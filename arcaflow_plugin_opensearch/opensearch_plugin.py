#!/usr/bin/env python3

import sys
import typing
from opensearchpy import OpenSearch

from arcaflow_plugin_sdk import plugin
from opensearch_schema import (
    ErrorOutput,
    SuccessOutput,
    BulkUploadList,
    BulkUploadObject,
    DocumentRequest,
    DataList,
    bulk_upload_object_schema,
)


@plugin.step(
    id="process_list",
    name="Process List",
    description="Process list input into a bulk_upload_list",
    outputs={"success": BulkUploadList, "error": ErrorOutput},
)
def process_list(
    params: DataList,
) -> typing.Tuple[str, typing.Union[BulkUploadList, ErrorOutput]]:
    bulk_upload_list = []
    for item in params.data_list:
        bulk_upload_list.append(BulkUploadObject(params.operation, item))
    return "success", BulkUploadList(bulk_upload_list)


@plugin.step(
    id="opensearch",
    name="OpenSearch",
    description="Load data into opensearch compatible instance",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def store(
    params: DocumentRequest,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    """
    The payload for the bulk upload function requires a list of objects,
    alternating such that the odd objects provide the Opensearch operation
    and operation metadata, and the even objects provide the JSON document
    to be uploaded using the operation from the previous object. Example:

    [
        {"create": {"_index": "myindex", "_id": "<id>"}},
        {"A JSON": "document"},
        {"index": {"_index": "myindex", "_id": "<id>"}},
        {"A JSON": "document"},
        {"delete": {"_index": "myindex", "_id": "<id>"}},
        {"A JSON": "document"},
    ]
    """

    def process_bulk_list_generator():
        for i in params.bulk_upload_list:
            # Create the operation and data document from the list
            item = list(bulk_upload_object_schema.serialize(i).values())
            operation = item[0]
            yield operation
            doc = item[1]
            # Append the global metadata to the document
            if params.metadata:
                doc["metadata"] = params.metadata
            yield doc

    if params.username:
        connection = OpenSearch(
            hosts=params.url,
            http_auth=(params.username, params.password),
            verify_certs=params.tls_verify,
        )
    # Support for servers that don't require authentication
    else:
        connection = OpenSearch(
            hosts=params.url,
            verify_certs=params.tls_verify,
        )

    try:
        resp = connection.bulk(
            body=process_bulk_list_generator(),
            index=params.default_index,
        )

        if resp["errors"]:
            shards = {}
            for i in resp["items"]:
                shards[list(i.values())[0]["_id"]] = list(i.values())[0]["_shards"]
            raise Exception(f"Document status: {str(shards)}")

        ids = []
        for i in resp["items"]:
            ids.append(list(i.values())[0]["_id"])

        return "success", SuccessOutput(
            "Successfully uploaded document(s).",
            ids,
        )

    except Exception as ex:
        return "error", ErrorOutput(f"Failed to create OpenSearch document(s): {ex}")


if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(store, process_list)))
