import os

from dotenv import load_dotenv
from snowflake.connector.connection import SnowflakeConnection

from dot_connect.backends.snowflake import connect, load_config


def test_load_config():
    loaded_configs = load_config()
    assert loaded_configs.get("account")


def test_connect():
    con = connect()
    load_dotenv(override=True)
    assert isinstance(con, SnowflakeConnection)
