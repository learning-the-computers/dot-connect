"""Tests for the MySQL connection utility in the dot_connect package."""

import dot_connect
from dot_connect import load_config


def test_load_config():
    """
    Test if the 'load_config' function retrieves valid MySQL configuration.

    The function should load a dictionary containing valid MySQL connection
    parameters. This test specifically checks for the presence of a 'password'
    key in the returned configuration.
    """
    loaded_configs = load_config("MYSQL")
    assert loaded_configs.get("password")


def test_connect():
    """
    Test a successful MySQL connection using the 'connect' function.

    The function should establish a connection to a MySQL database and
    be able to execute a simple query. This test checks if a basic "SELECT 1"
    query can be successfully executed.
    """
    con = dot_connect.mysql.connect()
    cursor = con.cursor()
    cursor.execute("SELECT 1")
    assert cursor.fetchall()
