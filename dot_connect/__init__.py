"""The module for making connections easier."""
from dot_connect.backends import load_config

try:
    from dot_connect.backends import mssql
except:  # noqa E722
    pass

try:
    from dot_connect.backends import mysql
except ImportError:
    pass

try:
    from dot_connect.backends import postgres
except ImportError:
    pass

try:
    from dot_connect.backends import snowflake
except ImportError:
    pass

try:
    from dot_connect.backends import snowpark
except ImportError:
    pass


def list_backends() -> list:
    """List compatible dot-connect backends."""
    return ["mssql", "mysql", "postgres", "snowflake", "snowpark"]


__all__ = ["load_config", "mssql", "mysql", "postgres", "snowflake", "snowpark"]
