"""Utility module to handle Snowflake-related configurations."""

from dot_connect.backends import load_config


def connect(**kwargs):
    """Connect to Snowpark using the environment variables."""
    from snowflake.snowpark import Session

    config = load_config("SNOWFLAKE")

    config.update(**kwargs)
    return Session.builder.configs(config).create()
