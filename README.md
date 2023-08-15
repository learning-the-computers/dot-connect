# dot-connect
[![tox](https://github.com/learning-the-computers/dot-connect/actions/workflows/tox.yml/badge.svg)](https://github.com/learning-the-computers/dot-connect/actions/workflows/tox.yml)

A Python package designed to simplify the way you fetch connection configurations and establish connections to various database and cloud systems.

## 🚀 Features

- **Unified Interface**: Single interface - no need to remember different APIs for databases or cloud providers.
- **Easy Configuration**: Fetch connection configurations from multiple sources like JSON files, environment variables, etc.
- **Supported Backends**: MySQL, Postgres, and Snowflake. More coming soon.

---

## 💽 Installation

```bash
pip install dot-connect
```

## 📚 Quickstart

1. Create a .env file.
```
SNOWFLAKE_ACCOUNT=orgname-accountname
SNOWFLAKE_USER=username
SNOWFLAKE_PASSWORD=password
```

2. Connect and query various backends!
```python
import dot_connect

con = dot_connect.snowflake.connect()
con.cursor().execute("SELECT 1;").fetchall()

con = dot_connect.snowpark.connect()
con.sql("SELECT 1").show()

con = dot_connect.mysql.connect()

cursor = con.cursor()
cursor.execute("SELECT 1")
cursor.fetchall()

con = dot_connect.postgres.connect()

cursor = con.cursor()
cursor.execute("SELECT 1")
cursor.fetchall()
```

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ⚖️ License
Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full text.
