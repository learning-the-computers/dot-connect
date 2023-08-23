"""Tests for the Snowflake connection utility in the dot_connect package."""

from typing import Any, Literal

import pytest
from dotenv import load_dotenv
from snowflake.connector import SnowflakeConnection

import dot_connect
from dot_connect import load_config

snowflake = pytest.importorskip("snowflake.connector")


@pytest.fixture(scope="module")
def connection():
    """Fixture to provide a Snowflake connection and handle teardown."""
    load_dotenv(override=True)
    con = dot_connect.snowflake.connect()
    yield con
    con.close()


@pytest.mark.parametrize("key", ["account", "user", "password", "database"])
def test_load_config(key):
    """Validate individual keys in the 'load_config' function for Snowflake configurations."""
    loaded_configs = load_config("SNOWFLAKE")
    assert key in loaded_configs


@pytest.mark.parametrize(
    "query, expected", [("SELECT 1", 1), ("SELECT 'test'", "test")]
)
def test_basic_query_execution(
    connection: Any,
    query: Literal["SELECT 1", "SELECT 'test'"],
    expected: Literal[1, "test"],
):
    """Test basic query execution on the Snowflake connection."""
    cursor = connection.cursor()
    cursor.execute(query)
    assert cursor.fetchone()[0] == expected
    cursor.close()


def test_invalid_config():
    """Test for failure when provided with invalid connection configurations."""
    with pytest.raises(Exception):  # Replace with the specific exception you expect
        dot_connect.snowflake.connect(account="nonexistent_account")


def test_connect_instance(connection: Any):
    """Assess the Snowflake connection instance type."""
    assert isinstance(connection, SnowflakeConnection)
