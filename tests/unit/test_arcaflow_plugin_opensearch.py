#!/usr/bin/env python3

import unittest
import opensearch_plugin
from arcaflow_plugin_sdk import plugin


class StoreTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            opensearch_plugin.StoreDocumentRequest(
                url="OPENSEARCH_URL",
                username="OPENSEARCH_USERNAME",
                password="OPENSEARCH_PASSWORD",
                index="another-index",
                data={
                    "key1": "interesting value",
                    "key2": "next value",
                },
            )
        )

        plugin.test_object_serialization(
            opensearch_plugin.SuccessOutput(
                "successfully uploaded document for index another-index"
            )
        )

        plugin.test_object_serialization(
            opensearch_plugin.ErrorOutput(
                "Failed to create OpenSearch document: BadRequestError(400,"
                " 'mapper_parsing_exception','failed to parse')"
            )
        )
    
    def test_convert_to_homogeneous_list(self):
        test_cases = [
            ["a", "b", "c"],  # all str
            ["a", "b", 1],  # One final int to convert to str
            [1.0, 1, "1"],  # str at end, so upconvert all to str
            ["1", 1, 1.0],
            ["1", 1, 1],
            [1, 1, "1"],
            [1, 1, 1],
            [1.0, 1, 1],
            [1, 1, 1.0],
        ]
        # Ensure they're all homogeneous
        for test_case in test_cases:
            validate_list_items_homogeous_type(
                self, opensearch_plugin.convert_to_homogenous_list(test_case)
            )
        # Ensure the type matches
        self.assertEqual(
            int, type(opensearch_plugin.convert_to_homogenous_list([1, 1, 1])[0])
        )
        self.assertEqual(
            float,
            type(opensearch_plugin.convert_to_homogenous_list([1, 1, 1.0])[0]),
        )
        self.assertEqual(
            str,
            type(opensearch_plugin.convert_to_homogenous_list([1, 1.0, "1.0"])[0]),
        )


def validate_list_items_homogeous_type(t, input_list):
    if len(input_list) == 0:
        return  # no problem with an empty list
    expected_type = type(input_list[0])
    for item in input_list:
        t.assertEqual(type(item), expected_type)



if __name__ == "__main__":
    unittest.main()
