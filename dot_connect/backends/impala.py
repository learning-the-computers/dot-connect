"""Utility module to handle Impala-related configurations."""

from impala.dbapi import connect as impala_connect

from dot_connect.backends import load_config


def connect(**kwargs):
    """
    Connect to Impala using the environment variables.

    This function establishes a connection to an Impala database using the
    specified connection parameters. It first loads a configuration dictionary
    containing default values and then updates it with any keyword arguments
    passed to the function. The resulting configuration is used to establish
    the Impala connection.

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        impala.dbapi.connect.Connection: A connection object representing the
        connection to the Impala database.

    Example:
        To connect to Impala using custom parameters:
        >>> connection = connect(user='my_user', password='my_password')

    Note:
        This function requires the 'impyla' package to be installed. Make sure
        to have the package installed before using this function.

    """
    config = load_config("IMPALA")

    config.update(**kwargs)

    return impala_connect(**config)
