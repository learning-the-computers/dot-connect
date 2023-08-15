from dot_connect.backends.snowflake import load_config
import os

os.environ["SNOWFLAKE_ACCOUNT"] = "ORG_NAME-ACC_NAME"


def test_load_config():
    loaded_configs = load_config()
    assert loaded_configs.get("account") == os.environ["SNOWFLAKE_ACCOUNT"]
