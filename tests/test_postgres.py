"""Tests for the Postgres connection utility in the dot_connect package."""

import dot_connect
from dot_connect import load_config


def test_load_config():
    """
    Validate the 'load_config' function for PostgreSQL configurations.

    This test ensures that the function retrieves a configuration containing
    essential connection parameters. Specifically, it checks for the presence of
    a 'password' key in the returned configuration for PostgreSQL.
    """
    loaded_configs = load_config("POSTGRES")
    assert loaded_configs.get("password")


def test_connect():
    """
    Assess the PostgreSQL connection via the 'connect' function.

    This test establishes a connection to a PostgreSQL database using the
    'connect' function. It then verifies the connection's functionality by
    executing a basic "SELECT 1" query and checking the results.
    """
    con = dot_connect.postgres.connect()
    cursor = con.cursor()
    cursor.execute("SELECT 1")
    assert cursor.fetchall()
