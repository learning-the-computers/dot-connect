"""Utility module to handle PostgreSQL-related configurations."""

import contextlib
import os

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def load_config():
    """
    Extract and returns PostgreSQL-related configuration from the environment variables.

    Scans the environment variables for keys that start with "POSTGRES" and constructs
    a dictionary of configurations. The resulting dictionary has keys that are derived
    from the environment variable keys by removing the "POSTGRES" prefix and converting
    to lowercase. The values remain unchanged.

    Returns:
        dict: A dictionary containing PostgreSQL-related configurations. For example,
              if the environment has a variable POSTGRES_USER="admin", the resulting
              dictionary will have {"user": "admin"}.

    Example:
        If the environment variables are:
        POSTGRES_USER="admin"
        POSTGRES_PASSWORD="secret"
        Then the output will be:
        {"user": "admin", "password": "secret"}
    """
    return {
        "_".join(k.split("_")[1:]).lower(): v
        for k, v in os.environ.items()
        if k.startswith("POSTGRES")
    }


def connect():
    """Connect to PostgreSQL using the environment variables."""
    import psycopg2

    config = load_config()
    return psycopg2.connect(**config)
