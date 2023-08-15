from dotenv import load_dotenv
from snowflake.connector.connection import SnowflakeConnection

import dot_connect


def test_load_config():
    loaded_configs = dot_connect.snowflake.load_config()
    assert loaded_configs.get("account")


def test_connect():
    con = dot_connect.snowflake.connect()
    load_dotenv(override=True)
    assert isinstance(con, SnowflakeConnection)
