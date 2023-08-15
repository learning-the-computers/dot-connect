"""Utility module to handle PostgreSQL-related configurations."""

from dot_connect.backends import load_config


def connect(**kwargs):
    """Connect to PostgreSQL using the environment variables."""
    import psycopg2

    config = load_config("POSTGRES")

    config.update(**kwargs)
    
    return psycopg2.connect(**config)
