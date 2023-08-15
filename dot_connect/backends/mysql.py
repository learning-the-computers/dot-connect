"""Utility module to handle MySQL-related configurations."""

import contextlib
import os

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def load_config():
    """
    Extract and returns MySQL-related configuration from the environment variables.

    Scans the environment variables for keys that start with "MYSQL" and constructs
    a dictionary of configurations. The resulting dictionary has keys that are derived
    from the environment variable keys by removing the "MYSQL" prefix and converting
    to lowercase. The values remain unchanged.

    Returns:
        dict: A dictionary containing PostgreSQL-related configurations. For example,
              if the environment has a variable POSTGRES_USER="admin", the resulting
              dictionary will have {"user": "admin"}.

    Example:
        If the environment variables are:
        MYSQL_USER="admin"
        MYSQL_PASSWORD="secret"
        Then the output will be:
        {"user": "admin", "password": "secret"}
    """
    return {
        "_".join(k.split("_")[1:]).lower(): v
        for k, v in os.environ.items()
        if k.startswith("MYSQL")
    }


def connect():
    """Connect to PostgreSQL using the environment variables."""
    import mysql.connector

    config = load_config()
    return mysql.connector.connect(**config)
