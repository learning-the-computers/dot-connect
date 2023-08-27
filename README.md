<div align="center">
  <img src="https://github.com/charleshardage/dot-connect/assets/119973756/7d52a0b4-a7c3-4df0-845d-0d73b0a20a42"><br>
</div>

-----------------

# dot-connect
[![pytest + coverage](https://github.com/learning-the-computers/dot-connect/actions/workflows/pytest_cov.yml/badge.svg)](https://github.com/learning-the-computers/dot-connect/actions/workflows/pytest_cov.yml)
[![codecov](https://codecov.io/github/learning-the-computers/dot-connect/graph/badge.svg?token=BRBGOLAYLE)](https://codecov.io/github/learning-the-computers/dot-connect)
[![PyPI](https://img.shields.io/pypi/v/dot-connect.svg)](https://pypi.org/project/dot-connect)

A Python package designed to simplify the way you fetch connection configurations and establish connections to various databases and cloud systems.

## 🚀 Features

- **Unified Interface**: Say goodbye to juggling multiple APIs. Enjoy a standardized interface, making connecting with various databases and cloud providers easier.

- **Easy Configuration**: Fetch connection configurations with ease. `dot_connect` supports various sources like JSON files, environment variables, and more, ensuring flexibility and adaptability for your projects.

- **Supported Backends**: Out-of-the-box support for popular systems such as MySQL, Postgres, and Snowflake. We're continuously working to expand this list.

- **Extensibility**: Designed with developers in mind, it's easy to extend and customize `dot_connect` for your needs.

## 📦 Installation (PyPI)

```bash
pip install dot-connect
```

## 🔧 Usage

Using `dot_connect` is intuitive and straightforward.

### Getting Things Set Up

Before you begin, you can configure your environment variables by using a `.env` file or an alternative method. Additionally, you can utilize default authorization patterns supported by your chosen backend. `dot-connect` will prioritize credentials in a `.env` file.

Below are step-by-step examples of how you can connect and query various backends:

#### Snowflake

```python
import dot_connect

con = dot_connect.snowflake.connect()
print(con.cursor().execute("SELECT 1;").fetchall())
```

#### MySQL
```python
import dot_connect

con = dot_connect.mysql.connect()
cursor = con.cursor()
cursor.execute("SELECT 1")
result = cursor.fetchall()
print(result)
```

#### PostgreSQL
```python
import dot_connect

con = dot_connect.postgres.connect()
cursor = con.cursor()
cursor.execute("SELECT 1")
result = cursor.fetchall()
print(result)
```

## 🤝 Contributing

We welcome contributions from the community. Whether it's a bug report, a new feature, or an improvement, your insights will help make `dot_connect` even better. For more details, please see our [contributing guidelines](docs/CONTRIBUTING.md).

## ⚖️ License
Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full text.
