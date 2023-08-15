"""Utility module to config file contents as dictionaries"""
from typing import Dict

def read_json(file : str) -> Dict:
    """
    Returns contents of .json file as dict.

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

    with open(file, 'r') as f:
        connection_parameters = json.load(f)

    return connection_parameters

def read_yaml(file : str) -> Dict:
    """
    Returns contents of .yaml or .yml file as dict.

    Returns:
        file: Absolute or relative path to .yaml/.yml file.

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
    import yaml

    with open(file, 'r') as f:
        connection_parameters = yaml.load(f, Loader = yaml.FullLoader)

    return connection_parameters

def read_py(file : str) -> Dict: # NOT STARTED
    """
    Returns contents of .py file as dict.

    Returns:
        file: Absolute or relative path to .py file.

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

def read_ini_conf_cfg(file : str) -> Dict:
    """
    Returns contents of .ini, .conf, or .cfg file as dict.

    Returns:
        file: Absolute or relative path to file.

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
    import configparser

    config = configparser.ConfigParser()
    content = config.read(file)
    connection_parameters = {s:dict(content.items(s)) for s in content.sections()}

    return connection_parameters