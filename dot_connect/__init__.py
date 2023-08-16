"""The module for making connections easier."""
from dot_connect.backends import load_config  # noqa F401

try:
    from dot_connect.backends import mssql  # noqa F401
except:  # noqa E722
    pass

try:
    from dot_connect.backends import mysql  # noqa F401
except ImportError:
    pass

try:
    from dot_connect.backends import postgres  # noqa F401
except ImportError:
    pass

try:
    from dot_connect.backends import snowflake  # noqa F401
except ImportError:
    pass

try:
    from dot_connect.backends import snowpark  # noqa F401
except ImportError:
    pass


def list_backends() -> list:
    """List compatible dot-connect backends."""
    return ["mssql", "mysql", "postgres", "snowflake", "snowpark"]
