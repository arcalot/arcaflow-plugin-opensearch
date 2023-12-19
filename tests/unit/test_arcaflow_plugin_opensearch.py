#!/usr/bin/env python3

import unittest
import opensearch_plugin
from opensearch_schema import (
    # Operation,
    BulkUploadObject,
    OperationMeta,
)
from arcaflow_plugin_sdk import plugin


class StoreTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            opensearch_plugin.DocumentRequest(
                url="OPENSEARCH_URL",
                username="OPENSEARCH_USERNAME",
                password="OPENSEARCH_PASSWORD",
                default_index="another-index",
                metadata={
                    "key1": "interesting value",
                    "key2": "next value",
                },
                bulk_upload_list=[
                    BulkUploadObject(
                        operation={
                            # Operation.INDEX: BulkUploadOperationMeta(
                            # Temporarily changing the key to a string in order to work
                            # around a workflow validation failure for the enum as a key
                            "index": OperationMeta(
                                _index="myotherindex",
                                _id="abc123",
                            ),
                        },
                        data={
                            "key1": "item 1 data value 1",
                            "key2": "item 1 data value 2",
                        },
                    ),
                    BulkUploadObject(
                        operation={
                            # Operation.CREATE: BulkUploadOperationMeta(),
                            # Temporarily changing the key to a string in order to work
                            # around a workflow validation failure for the enum as a key
                            "create": OperationMeta(),
                        },
                        data={
                            "key1": "item 2 data value 1",
                            "key2": "item 2 data value 2",
                        },
                    ),
                ],
            )
        )

        plugin.test_object_serialization(
            opensearch_plugin.SuccessOutput(
                "successfully uploaded document for index another-index",
                ["abcdefg", "hijklmn"],
            )
        )

        plugin.test_object_serialization(
            opensearch_plugin.ErrorOutput(
                "Failed to create OpenSearch document: BadRequestError(400,"
                " 'mapper_parsing_exception','failed to parse')"
            )
        )


if __name__ == "__main__":
    unittest.main()
