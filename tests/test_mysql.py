"""Tests for the MySQL connection utility in the dot_connect package."""

import mysql.connector
import pytest

import dot_connect
from dot_connect import load_config


@pytest.mark.skip(reason="Docker + MySQL")
def test_load_config():
    """
    Test if the 'load_config' function retrieves valid MySQL configuration.

    The function should load a dictionary containing valid MySQL connection
    parameters. This test specifically checks for the presence of a 'password'
    key in the returned configuration.
    """
    loaded_configs = load_config("MYSQL")
    assert loaded_configs.get("password")


@pytest.mark.skip(reason="Docker + MySQL")
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


@pytest.mark.skip(reason="Docker + MySQL")
def test_connection_type():
    """
    Test if the create_connection function returns an object of type mysql.connector.connection_cext.CMySQLConnection.

    This test invokes the create_connection function and checks the type of its return value.
    The test will pass if the returned object is an instance of mysql.connector.connection_cext.CMySQLConnection.
    Otherwise, it will fail with an informative error message.
    """
    con = dot_connect.mysql.connect()
    assert isinstance(
        con, mysql.connector.connection_cext.CMySQLConnection
    ), f"Expected a CMySQLConnection connection, got {type(con)}"
    con.close()
