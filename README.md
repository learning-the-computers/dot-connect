# dot-connect

A Python package designed to simplify the way you fetch connection configurations and establish connections to various database and cloud systems.

---

## 🚀 Features

- **Unified Interface**: Single interface - no need to remember different APIs for different databases or cloud providers.
- **Easy Configuration**: Fetch connection configurations from multiple sources like JSON files, environment variables, etc.
- **Supported Backends**: Snowflake. More coming soon.

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

2. Connect and query Snowflake!
```python
from dot_connect.backends.snowflake import connect, load_config

con = connect()
con.cursor().execute("SELECT 1;").fetchall()
```

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ⚖️ License
Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full text.
