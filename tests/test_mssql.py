import pytest
from dot_connect import load_config
from pyodbc import InterfaceError


def test_mssql_connect_valid():
    # Assuming you have a test MSSQL database setup
    conn = connect(load_config("MSSQL"))
    assert conn is not None
    conn.close()

def test_mssql_connect_invalid():
    with pytest.raises(InterfaceError):  # Typically, pyodbc raises this for connection issues
        connect(user='invalid_user', password='invalid_password', database='invalid_db')
