"""Tests for the MSSQL connection utility in the dot_connect package."""
import dot_connect


def test_mssql_connect_valid():
    """
    Test valid connection to MSSQL.

    This test assumes that a valid MSSQL test database is set up and
    will check if the connection can be established.
    """
    conn = dot_connect.mssql.connect()
    assert conn is not None
    conn.close()
