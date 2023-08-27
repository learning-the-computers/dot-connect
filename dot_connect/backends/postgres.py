"""Utility module to handle PostgreSQL-related configurations."""

import psycopg2

from dot_connect.backends import load_config


def connect(**kwargs) -> psycopg2.extensions.connection:
    """
    Connect to PostgreSQL using the environment variables.

    This function establishes a connection to a PostgreSQL database using the
    specified connection parameters. It first loads a configuration dictionary
    containing default values and then updates it with any keyword arguments
    passed to the function. The resulting configuration is used to establish
    the PostgreSQL connection.

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        psycopg2.extensions.connection: A connection object representing the
        connection to the PostgreSQL database.

    Example:
        To connect to PostgreSQL using custom parameters:
        >>> connection = connect(user='my_user', password='my_password', dbname='my_db')

    Note:
        This function requires the 'psycopg2' package to be installed. Make sure
        to have the package installed before using this function.

    """
    config = load_config("POSTGRES")

    config.update(**kwargs)

    return psycopg2.connect(**config)
