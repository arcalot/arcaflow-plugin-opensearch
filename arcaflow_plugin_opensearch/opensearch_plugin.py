#!/usr/bin/env python3

import sys
import typing

from opensearchpy import OpenSearch

from arcaflow_plugin_sdk import plugin
from opensearch_schema import ErrorOutput, SuccessOutput, StoreDocumentRequest


def convert_to_supported_type(value) -> typing.Dict:
    type_of_val = type(value)
    if type_of_val == list:
        new_list = []
        for i in value:
            new_list.append(convert_to_supported_type(i))
        # A list needs to be of a consistent type or it will
        # not be indexible into a system like Opensearch
        return convert_to_homogenous_list(new_list)
    elif type_of_val == dict:
        result = {}
        for k in value:
            result[convert_to_supported_type(k)] = convert_to_supported_type(value[k])
        return result
    elif type_of_val in (float, int, str, bool):
        return value
    elif isinstance(type_of_val, type(None)):
        return str("")
    else:
        print("Unknown type", type_of_val, "with val", str(value))
        return str(value)


def convert_to_homogenous_list(input_list: list):
    # To make all types in list homogeneous, we upconvert them
    # to the least commom type.
    # int -> float -> str
    # bool + None -> str
    list_type = str()
    for j in input_list:
        if type(j) in (str, bool, type(None)):
            list_type = str()
            break
        elif type(j) is float:
            list_type = float()
        elif type(j) is int and type(list_type) is not float:
            list_type = int()
    return list(map(type(list_type), input_list))


@plugin.step(
    id="opensearch",
    name="OpenSearch",
    description="Load data into opensearch compatible instance",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def store(
    params: StoreDocumentRequest,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    document = convert_to_supported_type(params.data)

    try:
        if params.username:
            opensearch = OpenSearch(
                hosts=params.url,
                http_auth=(params.username, params.password),
                verify_certs=params.tls_verify,
            )
        # Support for servers that don't require authentication
        else:
            opensearch = OpenSearch(
                hosts=params.url,
                verify_certs=params.tls_verify,
            )
        resp = opensearch.index(
            index=params.index,
            body=document,
        )
        if resp["result"] != "created":
            raise Exception(f"Document status: {resp['_shards']}")

        return "success", SuccessOutput(
            f"Successfully uploaded document for index {params.index}"
        )
    except Exception as ex:
        return "error", ErrorOutput(f"Failed to create OpenSearch document: {ex}")


if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(store)))
