"""Utility module to handle SQL Server-related configurations."""

import contextlib
import os

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def load_config():
    """
    Extract and returns SQL Server-related configuration from the environment variables.

    Scans the environment variables for keys that start with "SQLSERVER" and constructs
    a dictionary of configurations. The resulting dictionary has keys that are derived
    from the environment variable keys by removing the "SQLSERVER" prefix and converting
    to lowercase. The values remain unchanged.

    Returns:
        dict: A dictionary containing SQL Server-related configurations. For example,
              if the environment has a variable SQLSERVER_USER="admin", the resulting
              dictionary will have {"user": "admin"}.

    Example:
        If the environment variables are:
        SQLSERVER_USER="admin"
        SQLSERVER_PASSWORD="secret"
        SQLSERVER_DATABASE="mydatabase"
        SQLSERVER_SERVER="localhost"
        Then the output will be:
        {
            "user": "admin",
            "password": "secret",
            "database": "mydatabase",
            "server": "localhost"
        }
    """
    return {
        "_".join(k.split("_")[1:]).lower(): v
        for k, v in os.environ.items()
        if k.startswith("SQLSERVER")
    }


def connect():
    """Connect to SQL Server using the environment variables."""
    import pyodbc

    config = load_config()
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['user']};"
        f"PWD={config['password']}"
    )
    return pyodbc.connect(connection_string)
