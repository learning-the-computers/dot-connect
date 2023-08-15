"""Utility module to handle MySQL-related configurations."""

import contextlib

from dot_connect.backends import load_config

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def connect():
    """Connect to PostgreSQL using the environment variables."""
    import mysql.connector

    config = load_config("MYSQL")
    return mysql.connector.connect(**config)
