"""Utility module to handle MySQL-related configurations."""

import mysql.connector

from dot_connect.backends import load_config


def connect(**kwargs) -> mysql.connector.connection_cext.CMySQLConnection:
    """
    Connect to MySQL using environment variables.

    This function establishes a connection to a MySQL database using the specified
    connection parameters. It first loads a configuration dictionary containing
    default values and then updates it with any keyword arguments passed to the
    function. The resulting configuration is used to establish the MySQL connection.

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object representing
        the connection to the MySQL database.

    Example:
        To connect to MySQL using custom parameters:
        >>> connection = connect_mysql(user='my_user', password='my_password')

    Note:
        This function requires the 'mysql-connector-python' package to be installed.
        Make sure to have the package installed before using this function.

    """
    config = load_config("MYSQL")

    config.update(**kwargs)

    return mysql.connector.connect(**config)
