from dotenv import load_dotenv
from mysql.connector import MySQLConnection

import dot_connect


def test_load_config():
    loaded_configs = dot_connect.mysql.load_config()
    assert loaded_configs.get("password")


def test_connect():
    con = dot_connect.mysql.connect()
    cursor = con.cursor()
    cursor.execute("SELECT 1")
    assert cursor.fetchall()
