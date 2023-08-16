"""Tests for the MSSQL connection utility in the dot_connect package."""

import pytest
from pyodbc import InterfaceError

import dot_connect
from dot_connect import load_config


def test_mssql_connect_valid():
    """
    Test valid connection to MSSQL.

    This test assumes that a valid MSSQL test database is set up and
    will check if the connection can be established.
    """
    # Assuming you have a test MSSQL database setup
    conn = dot_connect.mssql.connect(load_config("MSSQL"))
    assert conn is not None
    conn.close()


def test_mssql_connect_invalid():
    """
    Test invalid connection to MSSQL.

    This test provides invalid user credentials to ensure that the
    expected InterfaceError is raised by pyodbc.
    """
    with pytest.raises(
        InterfaceError
    ):  # Typically, pyodbc raises this for connection issues
        dot_connect.mssql.connect(
            user="invalid_user", password="invalid_password", database="invalid_db"
        )
