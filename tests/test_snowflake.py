from dot_connect.backends.snowflake import load_config
from dot_connect.backends.snowflake import connect

from snowflake.connector.connection import SnowflakeConnection

from dotenv import load_dotenv

import os


def test_load_config():
    loaded_configs = load_config()
    assert loaded_configs.get("account")


def test_connect():
    con = connect()
    load_dotenv(override=True)
    assert isinstance(con, SnowflakeConnection)
