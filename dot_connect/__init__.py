"""The module for making connections easier."""
from dot_connect.backends import (  # noqa F401
    load_config,
    mssql,
    mysql,
    postgres,
    snowflake,
    snowpark,
)


def list_backends() -> list:
    """List compatible dot-connect backends."""
    return ["mssql", "mysql", "postgres", "snowflake", "snowpark"]
