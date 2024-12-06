import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from repositories.tweet_repo import TweetRepo
from utils.connector import DbConnector


class TestTweetRepo(unittest.TestCase):
    def setUp(self):
        # Set up the mock objects and the TweetRepo instance before each test
        self.mock_connection = MagicMock()
        self.mock_db_connector = MagicMock()
        # This line mocks the database 
        # We dont actual use the db but only the code itself
        self.mock_db_connector.connection = self.mock_connection
        self.tweet_repo = TweetRepo(self.mock_db_connector)

    def test_get_all(self):
        # Test retrieving all tweets from the database

        # Arrange: Set up the mock database cursor and its behavior
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("1", "test tweet", "2024-12-01"),
            ("2", "another tweet", "2024-12-02"),
        ]
        mock_cursor.description = [("id",), ("content",), ("created_at",)]
        self.mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        expected_result = [
            {"id": "1", "content": "test tweet", "created_at": "2024-12-01"},
            {"id": "2", "content": "another tweet", "created_at": "2024-12-02"},
        ]

        # Act: Call the method to be tested
        result = self.tweet_repo.get_all()

        # Assert: Verify the output
        self.assertEqual(result, expected_result)

    def test_get_all_database_error(self):
        # Test that an exception is raised when the database encounters an error

        # Arrange: Simulate a database error
        self.mock_connection.cursor.return_value.__enter__.side_effect = Exception("Database error")

        # Act & Assert: Ensure an exception is raised and contains the correct message
        with self.assertRaises(Exception) as context:
            self.tweet_repo.get_all()
        self.assertIn("Database error", str(context.exception))

    def test_get_tweet_by_id_success(self):
        # Test successfully retrieving a tweet by its ID

        # Arrange: Set up the mock database cursor and its behavior
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (1, "Sample tweet", "2024-12-01")
        mock_cursor.description = [("id",), ("content",), ("created_at",)]
        self.mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        expected_result = {"id": 1, "content": "Sample tweet", "created_at": "2024-12-01"}

        # Act: Call the method to be tested
        result = self.tweet_repo.get_tweet_by_id(1)

        # Assert: Verify the output
        self.assertEqual(result, expected_result)

    def test_get_tweet_by_id_not_found(self):
        # Test retrieving a tweet by ID when it does not exist

        # Arrange: Simulate a case where no tweet is found
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_cursor.description = [("id",), ("content",), ("created_at",)]
        self.mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Act: Call the method to be tested
        result = self.tweet_repo.get_tweet_by_id(99)

        # Assert: Verify that an empty dictionary is returned
        self.assertEqual(result, {})

    def test_check_if_saved_true(self):
        # Test if a tweet exists in the database and returns True

        # Arrange: Simulate a case where the tweet exists
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        self.mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Act: Call the method to be tested
        result = self.tweet_repo.check_if_saved(1)

        # Assert: Verify that the result is True
        self.assertTrue(result)

    def test_check_if_saved_false(self):
        # Test if a tweet does not exist in the database and returns False

        # Arrange: Simulate a case where the tweet does not exist
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []  # Simulate no records
        self.mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Act: Call the method to be tested
        result = self.tweet_repo.check_if_saved(1)

        # Assert: Verify that the result is False
        self.assertFalse(result)