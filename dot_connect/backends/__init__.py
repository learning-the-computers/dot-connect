"""Module containing backend specific logic."""
import contextlib
import os
from typing import Any, Dict, Optional, Union

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv(override=True)


def read_json(file: str) -> Dict:
    """
    Return contents of .json file as dict.

    Returns:
        file: Absolute or relative path to .json file.

    Example:
        If the json file contains:
        {
            "account": "abc.us-east-1",
            "user": "JSMITH",
            "password": "password123"
        }
        then returned dict will be
        {
            "account": "abc.us-east-1",
            "user": "JSMITH",
            "password": "password123"
        }
    """
    import json

    with open(file) as f:
        connection_parameters = json.load(f)

    return connection_parameters


def read_yaml(file: str) -> Dict:
    """
    Return contents of .yaml or .yml file as dict.

    Returns:
        file: Absolute or relative path to .yaml/.yml file.

    Example:
        "account": "abc.us-east-1",
        "user": "JSMITH",
        "password": "password123"
        then returned dict will be
        {
            "account": "abc.us-east-1",
            "user": "JSMITH",
            "password": "password123"
        }
    """
    import yaml

    with open(file) as f:
        connection_parameters = yaml.load(f, Loader=yaml.FullLoader)

    return connection_parameters


def read_ini_conf_cfg(file: str) -> Dict:
    """
    Return contents of .ini, .conf, or .cfg file as dict.

    Returns:
        file: Absolute or relative path to file.

    Example:
        If the json file contains:
        ['credentials']
        "account": "abc.us-east-1",
        "user": "JSMITH",
        "password": "password123"
        then returned dict will be
        {credentials:
            {
            "account": "abc.us-east-1",
            "user": "JSMITH",
            "password": "password123"
            }
        }
    """
    import configparser

    config = configparser.ConfigParser()
    config.read(file)
    return {s: dict(config.items(s)) for s in config.sections()}


def parse_file(file: str, *args) -> Union[Dict[Any, Any], str]:
    """
    Return contents of supported file format.

    Values passed as *args will be treated as nested keys.
    Currently supported file formats are
    '.json', '.yaml', '.yml', '.ini', '.cfg', '.conf'.

    Returns:
        file: Absolute or relative path to file.

    """
    if not isinstance(file, str):
        raise TypeError("File argument must be string.")

    if file.endswith(".json"):
        connection_parameters = read_json(file)
    elif file.endswith((".yml", ".yaml")):
        connection_parameters = read_yaml(file)
    elif file.endswith((".ini", ".cfg", ".conf")):
        connection_parameters = read_ini_conf_cfg(file)
    else:
        supported_types = (".json", ".yaml", ".yml", ".ini", ".cfg", ".conf")
        return f"File must be of type {supported_types}."
    if args:  # Traverse any nested keys passed
        for k in args:
            if k in connection_parameters:
                connection_parameters = connection_parameters[k]
            else:
                return connection_parameters
    return connection_parameters


def load_config(prefix: str, file: Optional[str] = None, *args):
    """
    Extract and returns configuration from the env variables or local config file.

    For environment variables:
    Scans the environment variables for keys that start with "SNOWFLAKE" and constructs
    a dictionary of configurations. The resulting dictionary has keys that are derived
    from the environment variable keys by removing the "SNOWFLAKE" prefix and converting
    to lowercase. The values remain unchanged.

    For local config file:
    Unpacks config file based on file extensions. Supported file types are
    .json, .yaml, .yml, .ini, .cfg, .conf.

    Returns:
        dict: A dictionary containing Snowflake-related configurations. For example,
              if the environment has a variable SNOWFLAKE_USER="admin", the resulting
              dictionary will have {"user": "admin"}.
        file: A file path to a config file holding credentials.

    Example:
        If the environment variables are:
        SNOWFLAKE_USER="admin"
        SNOWFLAKE_PASSWORD="secret"
        Then the output will be:
        {"user": "admin", "password": "secret"}
    """
    if prefix:
        prefix = prefix.upper()
        return {
            "_".join(k.split("_")[1:]).lower(): v
            for k, v in os.environ.items()
            if k.upper().startswith(prefix)
        }

    if file:
        return parse_file(file, *args)
