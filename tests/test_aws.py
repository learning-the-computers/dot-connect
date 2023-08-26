"""Tests for the AWS connection utility in the dot_connect package."""
from unittest.mock import patch

import dot_connect


def test_connect_fallback_to_client_on_unknown_service():
    """Test that the connect function falls back to boto3.client when boto3.resource  raises an exception."""
    service_name = "unrecognized_service"

    # Mocking boto3's resource and client functions
    with patch("boto3.resource", side_effect=Exception), patch(
        "boto3.client", return_value="client_result"
    ) as mock_client:
        result = dot_connect.aws.connect(service_name, some_key="some_value")

    mock_client.assert_called_once_with(service_name, some_key="some_value")
    assert result == "client_result"
