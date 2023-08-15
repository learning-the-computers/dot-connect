from dotenv import load_dotenv
from snowflake.snowpark import Session

from dot_connect.backends.snowpark import connect, load_config


def test_load_config():
    loaded_configs = load_config()
    assert loaded_configs.get("account")


def test_connect():
    con = connect()
    load_dotenv(override=True)
    assert isinstance(con, Session)
