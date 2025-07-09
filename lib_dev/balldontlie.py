"""
Balldontlie API client library.

This module provides a wrapper around the Balldontlie API for NBA data retrieval.
"""

from balldontlie import BalldontlieAPI
from balldontlie.exceptions import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError,
    BallDontLieException,
)
from dotenv import load_dotenv
import os
from typing import List, Optional, Any


load_dotenv()


class BalldontlieLib:
    """
    A wrapper class for the Balldontlie API.

    This class provides methods to interact with the Balldontlie API
    for retrieving NBA data such as teams, players, and games.
    """

    def __init__(self) -> None:
        """
        Initialize the Balldontlie API client.

        Initializes the API client using the BALLDONTLIE_API_KEY
        environment variable.

        Raises:
            ValueError: If the API key is not found in environment variables
        """
        api_key = os.getenv("BALLDONTLIE_API_KEY")
        if not api_key:
            raise ValueError("BALLDONTLIE_API_KEY environment variable is required")

        self.api = BalldontlieAPI(api_key=api_key)

    def get_teams(self) -> Optional[List[Any]]:
        """
        Retrieve all NBA teams from the API.

        Fetches the complete list of NBA teams from the Balldontlie API.

        Returns:
            List of team objects if successful, None if an error occurs

        Raises:
            AuthenticationError: If the API key is invalid
            RateLimitError: If the API rate limit is exceeded
            ValidationError: If the request parameters are invalid
            NotFoundError: If the resource is not found
            ServerError: If there's a server-side error
            BallDontLieException: For other API-related errors
        """
        try:
            print("Getting teams...")
            return self.api.nba.teams.list().data
        except AuthenticationError as e:
            print(
                f"Invalid API key. Status: {e.status_code}, Details: {e.response_data}"
            )
        except RateLimitError as e:
            print(
                f"Rate limit exceeded. Status: {e.status_code}, Details: {e.response_data}"
            )
        except ValidationError as e:
            print(
                f"Invalid request parameters. Status: {e.status_code}, Details: {e.response_data}"
            )
        except NotFoundError as e:
            print(
                f"Resource not found. Status: {e.status_code}, Details: {e.response_data}"
            )
        except ServerError as e:
            print(
                f"API server error. Status: {e.status_code}, Details: {e.response_data}"
            )
        except BallDontLieException as e:
            print(
                f"General API error. Status: {e.status_code}, Details: {e.response_data}"
            )
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

        return None
