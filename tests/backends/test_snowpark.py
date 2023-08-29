"""Tests for the Snowpark connection utility in the dot_connect package."""

import pytest
from dotenv import load_dotenv
from snowflake.snowpark import Session

import dot_connect
from dot_connect import load_config


@pytest.fixture(scope="module")
def snowpark_session():
    """Fixture to provide a Snowpark session and handle teardown."""
    load_dotenv(override=True)
    session = dot_connect.snowpark.connect()
    yield session
    session.close()


@pytest.mark.parametrize("key", ["account", "user", "password", "database"])
def test_load_config(key):
    """Validate individual keys in the 'load_config' function for Snowflake configurations."""
    loaded_configs = load_config("SNOWFLAKE")
    assert key in loaded_configs


def test_valid_session_instance(snowpark_session):
    """Test if the connection results in a valid Snowpark session instance."""
    assert isinstance(snowpark_session, Session)


@pytest.mark.parametrize(
    "config, exception",
    [
        (
            {"account": "nonexistent_account"},
            Exception,
        ),  # Replace with the specific exception you expect
        (
            {"user": "wrong_user"},
            Exception,
        ),  # Add more incorrect config cases as needed
    ],
)
def test_invalid_config(config, exception):
    """Test for failure when provided with invalid Snowpark session configurations."""
    with pytest.raises(exception):
        dot_connect.snowpark.connect(**config)
