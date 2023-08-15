"""Utility module to handle Snowflake-related configurations."""

import contextlib
import os

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def load_config():
    """
    Extract and returns Snowpark-related configuration from the environment variables.

    Scans the environment variables for keys that start with "SNOWFLAKE" and constructs
    a dictionary of configurations. The resulting dictionary has keys that are derived
    from the environment variable keys by removing the "SNOWFLAKE" prefix and converting
    to lowercase. The values remain unchanged.

    Returns:
        dict: A dictionary containing Snowflake-related configurations. For example,
              if the environment has a variable SNOWFLAKE_USER="admin", the resulting
              dictionary will have {"user": "admin"}.

    Example:
        If the environment variables are:
        SNOWFLAKE_USER="admin"
        SNOWFLAKE_PASS="secret"
        Then the output will be:
        {"user": "admin", "pass": "secret"}
    """
    return {
        "_".join(k.split("_")[1:]).lower(): v
        for k, v in os.environ.items()
        if k.startswith("SNOWFLAKE")
    }

def connect():
    """Connect to Snowpark using the environment variables."""
    from snowflake.snowpark import Session

    config = load_config()
    return Session.builder.configs(config).create() 