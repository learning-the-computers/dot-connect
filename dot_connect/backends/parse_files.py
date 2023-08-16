"""Utility module to config file contents as dictionaries"""
from typing import Dict

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

    with open(file, "r") as f:
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

    with open(file, "r") as f:
        connection_parameters = yaml.load(f, Loader = yaml.FullLoader)

    return connection_parameters

# def read_py(file : str) -> Dict: # NOT STARTED
#     """
#     Returns contents of .py file as dict.

#     Returns:
#         file: Absolute or relative path to .py file.

#     Example:
#         If the json file contains:
#         {
#         "account": "abc.us-east-1",
#         "user": "JSMITH",
#         "password": "password123"
#         }
#         then returned dict will be
#         {
#         "account": "abc.us-east-1",
#         "user": "JSMITH",
#         "password": "password123"
#         }
#     """
#     import json
#     with open(file) as f:
#         connection_parameters = json.load(f)

#     return connection_parameters

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
    connection_parameters = {s:dict(config.items(s)) for s in config.sections()}

    return connection_parameters

def parse_file(file: str, *args) -> Dict:
    """
    Return contents of supported file format.

    Values passed as *args will be treated as nested keys.
    Currently supported file formats are
    '.json', '.yaml', '.yml', '.ini', '.cfg', '.conf'.

    Returns:
        file: Absolute or relative path to file.

    """
    if isinstance(file, str):
        supported_types = (".json", ".yaml", ".yml", ".ini", ".cfg", ".conf")
        if file.endswith(".json"):
            connection_parameters = read_json(file)
        elif file.endswith((".yml", ".yaml")):
            connection_parameters = read_yaml(file)
        elif file.endswith((".ini", ".cfg", ".conf")):
            connection_parameters = read_yaml(file)
        else:
            return f"File must be of type {supported_types}."
    else:
        raise TypeError("File argument must be string.")
    
    if args: # Traverse any nested keys passed
        for k in args:
            if k in connection_parameters:
                connection_parameters = connection_parameters[k]
            else:
                return connection_parameters
        return connection_parameters
    else:
        return connection_parameters