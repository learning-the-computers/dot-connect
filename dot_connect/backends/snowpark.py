"""Utility module to handle Snowflake-related configurations."""

import contextlib

from dot_connect.backends import load_config

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def connect():
    """Connect to Snowpark using the environment variables."""
    from snowflake.snowpark import Session

    config = load_config("SNOWFLAKE")
    return Session.builder.configs(config).create()
