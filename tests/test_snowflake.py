"""Tests for the Snowflake connection utility in the dot_connect package."""

from dotenv import load_dotenv
from snowflake.connector.connection import SnowflakeConnection

import dot_connect
from dot_connect import load_config


def test_load_config():
    """
    Validate the 'load_config' function for Snowflake configurations.

    This test ensures that the function retrieves a configuration containing
    essential connection parameters for Snowflake. Specifically, it verifies
    the presence of an 'account' key in the returned configuration.
    """
    loaded_configs = load_config("SNOWFLAKE")
    assert loaded_configs.get("account")


def test_connect():
    """
    Assess the Snowflake connection via the 'connect' function.

    This test establishes a connection to Snowflake using the 'connect' function
    and then checks if the returned connection is an instance of the
    `SnowflakeConnection` class. Environment variables are loaded for the
    connection.
    """
    con = dot_connect.snowflake.connect()
    load_dotenv(override=True)
    assert isinstance(con, SnowflakeConnection)


def test_basic_query_execution():
    """
    Test basic query execution on the Snowflake connection.

    This test establishes a connection, runs a basic query to ensure
    functionality, and then disconnects.
    """
    con = dot_connect.snowflake.connect()
    load_dotenv(override=True)
    cursor = con.cursor()
    cursor.execute("SELECT 1")
    assert cursor.fetchone()[0] == 1
    cursor.close()
    con.close()
