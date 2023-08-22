"""The module for making connections easier."""
import contextlib

from dot_connect.backends import load_config

with contextlib.suppress(ImportError):
    from dot_connect.backends import aws
with contextlib.suppress(ImportError):
    from dot_connect.backends import azure
with contextlib.suppress(Exception):
    from dot_connect.backends import impala
with contextlib.suppress(Exception):
    from dot_connect.backends import mssql
with contextlib.suppress(ImportError):
    from dot_connect.backends import mysql
with contextlib.suppress(ImportError):
    from dot_connect.backends import postgres
with contextlib.suppress(ImportError):
    from dot_connect.backends import snowflake
with contextlib.suppress(ImportError):
    from dot_connect.backends import snowpark

def list_backends() -> list:
    """List compatible dot-connect backends."""
    return [
        "aws",
        "azure",
        "impala",
        "mssql",
        "mysql",
        "postgres",
        "snowflake",
        "snowpark",
    ]


__all__ = [
    "load_config",
    "aws",
    "azure",
    "impala",
    "mssql",
    "mysql",
    "postgres",
    "snowflake",
    "snowpark",
]
