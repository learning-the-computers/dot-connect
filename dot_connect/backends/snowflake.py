"""Utility module to handle Snowflake-related configurations."""

import contextlib
import os
from configparser import ConfigParser

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def load_config():
    """
    Extract and returns Snowflake-related configuration from the environment variables.

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
        SNOWFLAKE_PASSWORD="secret"
        Then the output will be:
        {"user": "admin", "password": "secret"}
    """
    return {
        "_".join(k.split("_")[1:]).lower(): v
        for k, v in os.environ.items()
        if k.startswith("SNOWFLAKE")
    }


def load_snowsql_config():
    """
    Load configuration from the ~/.snowsql/config file.

    Returns:
        dict: A dictionary containing the SnowSQL configurations. Each section
              in the config will be a key in the dictionary, and its value will
              be another dictionary containing that section's key-value pairs.

    Example:
        If the config file contains:
        [connections.myconn]
        accountname = my_account
        username = my_user

        The output will be:
        {
            "connections.myconn": {
                "accountname": "my_account",
                "username": "my_user"
            }
        }
    """
    config_path = os.path.expanduser("~/.snowsql/config")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    parser = ConfigParser()
    parser.read(config_path)

    config_data = {}
    for section in parser.sections():
        config_data[section] = dict(parser.items(section))

    return config_data


def connect(**kwargs):
    """Connect to Snowflake using the environment variables."""
    import snowflake.connector

    config = load_config()

    config.update(**kwargs)

    return snowflake.connector.connect(**config)
