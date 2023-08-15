from dotenv import load_dotenv
from snowflake.connector.connection import SnowflakeConnection

import dot_connect
from dot_connect import load_config


def test_load_config():
    loaded_configs = load_config("SNOWFLAKE")
    assert loaded_configs.get("account")


def test_connect():
    con = dot_connect.snowflake.connect()
    load_dotenv(override=True)
    assert isinstance(con, SnowflakeConnection)
