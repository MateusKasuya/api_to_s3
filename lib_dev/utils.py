"""
Utility enums for the Smartbetting project.

This module contains enumeration classes for defining constants used
throughout the Smartbetting data pipeline.
"""

from enum import Enum


class Bucket(Enum):
    """
    S3 bucket enumeration.

    Defines the available S3 buckets for data storage.
    """

    LAKE_SMARTBETTING = "lake-smartbetting"

    def __str__(self) -> str:
        """
        Return the string representation of the bucket value.

        Returns:
            String value of the bucket
        """
        return "%s" % self.value


class Catalog(Enum):
    """
    Data catalog enumeration.

    Defines the available data catalogs for organizing data.
    """

    NBA = "nba"

    def __str__(self) -> str:
        """
        Return the string representation of the catalog value.

        Returns:
            String value of the catalog
        """
        return "%s" % self.value


class Schema(Enum):
    """
    Data schema enumeration.

    Defines the available data schemas for data quality layers.
    """

    BRONZE = "bronze"

    def __str__(self) -> str:
        """
        Return the string representation of the schema value.

        Returns:
            String value of the schema
        """
        return "%s" % self.value


class Table(Enum):
    """
    Data table enumeration.

    Defines the available data tables for specific entities.
    """

    TEAMS = "teams"

    def __str__(self) -> str:
        """
        Return the string representation of the table value.

        Returns:
            String value of the table
        """
        return "%s" % self.value
