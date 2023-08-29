"""This module provides utilities for parsing backend configuration."""

import json

import yaml

from dot_connect import list_backends, load_config, parse_file, read_json, read_yaml


def test_read_json(tmp_path):
    """Test the read_json function with valid JSON data."""
    data = {"key": "value"}
    file_path = tmp_path / "data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)

    result = read_json(file_path)
    assert result == data


def test_read_yaml(tmp_path):
    """Test the read_yaml function with valid YAML data."""
    data = {"key": "value"}
    file_path = tmp_path / "data.yaml"
    with open(file_path, "w") as f:
        yaml.dump(data, f)

    result = read_yaml(file_path)
    assert result == data


def test_parse_file_json(tmp_path):
    """Test the parse_file function for JSON file type."""
    data = {"key": "value"}
    file_path = tmp_path / "data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)

    result = parse_file(str(file_path))
    assert result == data


def test_parse_file_unsupported_type(tmp_path):
    """Test the parse_file function for unsupported file types."""
    file_path = tmp_path / "data.txt"
    file_path.write_text("just some text")

    result = parse_file(str(file_path))
    assert (
        result
        == "File must be of type ('.json', '.yaml', '.yml', '.ini', '.cfg', '.conf')."  # noqa: W503
    )


def test_load_config_from_file_json(tmp_path):
    """Test the load_config function with a JSON configuration file."""
    data = {"key": "value"}
    file_path = tmp_path / "data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)

    result = load_config("", str(file_path))
    assert result == data


def test_list_backends():
    """Test the list_backends function to ensure all backends are listed correctly."""
    backends = list_backends()
    expected_backends = [
        "aws",
        "azure",
        "mssql",
        "mysql",
        "postgres",
        "pyspark",
        "snowflake",
        "snowpark",
    ]
    assert backends == expected_backends
