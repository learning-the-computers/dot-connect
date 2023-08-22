"""Utility module to handle Snowflake-related configurations."""

import os

from dot_connect.backends import load_config


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
    from dot_connect import read_ini_conf_cfg

    config_path = os.path.expanduser("~/.snowsql/config")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    return read_ini_conf_cfg(config_path)


def connect(**kwargs):
    """
    Connect to Snowflake using the environment variables.

    Using the specified connection parameters, this function establishes a
    connection to a Snowflake database. It first loads a configuration dictionary
    containing default values and then updates it with any keyword arguments
    passed to the function. The resulting configuration is used to establish
    the Snowflake connection.

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        snowflake.connector.connection.SnowflakeConnection: A connection object
        representing the connection to the Snowflake database.

    Example:
        To connect to Snowflake using custom parameters:
        >>> connection = connect(user='my_user', password='my_password', ...)

    Note:
        This function requires the 'snowflake-connector-python' package to be
        installed. Make sure to have the package installed before using this
        function.

    """
    import snowflake.connector

    config = load_config("SNOWFLAKE")

    config.update(**kwargs)

    return snowflake.connector.connect(**config)
