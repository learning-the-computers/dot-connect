"""Tests for the various utilities in the dot_connect package."""

from dot_connect.backends import parse_file

# Sample content for JSON, YAML, and INI files
json_content = """
{
    "account": "abc.us-east-1",
    "user": "JSMITH",
    "password": "password123"
}
"""

yaml_content = """
account: "abc.us-east-1"
user: "JSMITH"
password: "password123"
"""

ini_content = """
[credentials]
account = abc.us-east-1
user = JSMITH
password = password123
"""


def test_read_json(tmp_path):
    """Test reading of JSON content from a sample JSON file using the `parse_file` function."""
    file = tmp_path / "config.json"
    file.write_text(json_content)
    result = parse_file(str(file))
    assert result == {
        "account": "abc.us-east-1",
        "user": "JSMITH",
        "password": "password123",
    }


def test_read_yaml(tmp_path):
    """Test reading of YAML content from a sample YAML file using the `parse_file` function."""
    file = tmp_path / "config.yaml"
    file.write_text(yaml_content)
    result = parse_file(str(file))
    assert result == {
        "account": "abc.us-east-1",
        "user": "JSMITH",
        "password": "password123",
    }


def test_read_ini(tmp_path):
    """Test reading of INI content from a sample INI file using the `parse_file` function."""
    file = tmp_path / "config.ini"
    file.write_text(ini_content)
    result = parse_file(str(file))
    assert result == {
        "credentials": {
            "account": "abc.us-east-1",
            "user": "JSMITH",
            "password": "password123",
        }
    }
