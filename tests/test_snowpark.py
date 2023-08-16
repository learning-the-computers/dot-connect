"""Tests for the Snowpark connection utility in the dot_connect package."""

from dotenv import load_dotenv
from snowflake.snowpark import Session

import dot_connect
from dot_connect import load_config


def test_load_config():
    """
    Test valid connection parameters.

    This test assumes that connection parameters work.
    """
    loaded_configs = load_config("SNOWFLAKE")
    assert loaded_configs.get("account")


def test_connect():
    """
    Test valid connection parameters.

    This test assumes that connection parameters work.
    """
    con = dot_connect.snowpark.connect()
    load_dotenv(override=True)
    assert isinstance(con, Session)
