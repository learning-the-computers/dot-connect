from dotenv import load_dotenv
from mysql.connector import MySQLConnection

import dot_connect
from dot_connect.backends import load_config


def test_load_config():
    loaded_configs = load_config("MYSQL")
    assert loaded_configs.get("password")


def test_connect():
    con = dot_connect.mysql.connect()
    cursor = con.cursor()
    cursor.execute("SELECT 1")
    assert cursor.fetchall()
