"""Utility module to handle MySQL-related configurations."""

from dot_connect.backends import load_config


def connect():
    """Connect to PostgreSQL using the environment variables."""
    import mysql.connector

    config = load_config("MYSQL")
    return mysql.connector.connect(**config)
