"""The module for making connections easier."""
from dot_connect.backends import load_config, mysql, postgres, snowflake, snowpark


def list_backends() -> list:
    """List compatible dot-connect backends."""
    return ["mysql", "postgres", "snowflake", "snowpark"]
