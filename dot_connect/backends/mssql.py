"""Utility module to handle Microsoft SQL Server-related configurations."""

import contextlib

with contextlib.suppress(ImportError):
    import pyodbc
from dot_connect.backends import load_config


def connect(**kwargs):
    """
    Establish a connection to a MSSQL database.

    The function fetches default connection configurations and optionally updates
    them with provided keyword arguments.

    Args:
        **kwargs: Connection parameters to override default configurations.

    Returns:
        pyodbc.Connection: Connection to the MSSQL database.

    Example:
        >>> connection = connect(user='my_user',
        >>>                      password='my_password',
        >>>                      database='my_db')

    Note:
        Ensure 'pyodbc' package is installed and relevant ODBC drivers
        for MSSQL are set up before utilizing this function.
    """
    config = load_config("MSSQL")

    config.update(kwargs)

    connection_string = ";".join([f"{key}={value}" for key, value in config.items()])

    return pyodbc.connect(connection_string)
