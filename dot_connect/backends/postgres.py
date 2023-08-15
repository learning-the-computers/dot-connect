"""Utility module to handle PostgreSQL-related configurations."""

import contextlib

from dot_connect.backends import load_config

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def connect():
    """Connect to PostgreSQL using the environment variables."""
    import psycopg2

    config = load_config("POSTGRES")
    return psycopg2.connect(**config)
