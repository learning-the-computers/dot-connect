"""Tests for the Azure connection utility in the dot_connect package."""
import unittest
from unittest.mock import patch

import pytest

import dot_connect


class TestAzureBlobStorageUtility(unittest.TestCase):
    """Test the Azure Blob Storage utility functions."""

    @patch("dot_connect.load_config")
    @pytest.mark.skip(reason="Need to figure out how to test this.")
    def test_connect_blob_service_loads_config(self, mock_load_config):
        """Test that the connect_blob_service function loads the config."""
        mock_load_config.return_value = {"dummy_key": "dummy_value"}

        dot_connect.azure.connect_blob_service()

        mock_load_config.assert_called_once_with("AZURE_BLOB_STORAGE")


if __name__ == "__main__":
    unittest.main()
