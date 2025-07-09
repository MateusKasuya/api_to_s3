"""
Smartbetting utility library.

This module provides utilities for data conversion and S3 operations
for the Smartbetting project.
"""

import boto3
import json
from typing import Any, List, Union


class SmartbettingLib:
    """
    Utility class for Smartbetting data operations.

    This class provides methods for converting data formats and
    uploading data to S3 storage.
    """

    def convert_to_json(self, data: Union[List[dict], dict]) -> str:
        """
        Convert data to JSON format.

        Args:
            data: Data to be converted to JSON. Can be a list of dictionaries
                  or a single dictionary.

        Returns:
            JSON string representation of the data

        Raises:
            TypeError: If the data cannot be serialized to JSON
        """
        print("Converting to JSON...")
        return json.dumps(data, indent=2)

    def convert_object_to_dict(self, objects: List[Any]) -> List[dict]:
        """
        Convert a list of objects to a list of dictionaries.

        Args:
            objects: List of objects that have a model_dump() method

        Returns:
            List of dictionaries converted from the objects

        Raises:
            AttributeError: If objects don't have model_dump() method
        """
        print("Converting object to dict...")
        return [data.model_dump() for data in objects]

    def upload_json_to_s3(
        self, json_data: str, bucket_name: Union[str, Any], key: Union[str, Any]
    ) -> None:
        """
        Upload JSON data to S3 bucket.

        Args:
            json_data: JSON string to upload
            bucket_name: Name of the S3 bucket (can be enum or string)
            key: S3 object key/path (can be enum or string)

        Returns:
            None

        Raises:
            boto3.exceptions.BotoCoreError: If there's an issue with AWS credentials
            boto3.exceptions.ClientError: If there's an S3 operation error
        """
        print("Uploading JSON to S3...")
        s3_client = boto3.client("s3")

        s3_client.put_object(
            Bucket=str(bucket_name),
            Key=str(key),
            Body=json_data,
            ContentType="application/json",
        )
        print("JSON uploaded to S3!!!")
