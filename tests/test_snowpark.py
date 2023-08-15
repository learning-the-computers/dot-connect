from dotenv import load_dotenv
from snowflake.snowpark import Session

import dot_connect


def test_load_config():
    loaded_configs = dot_connect.snowpark.load_config()
    assert loaded_configs.get("account")


def test_connect():
    con = dot_connect.snowpark.connect()
    load_dotenv(override=True)
    assert isinstance(con, Session)
