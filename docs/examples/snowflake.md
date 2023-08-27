---
hide:
  - toc
---

# Snowflake
Snowflake provides great documentation to help users get started with the Snowflake
Connector for Python if you're
[Connecting Using the Default Authenticator](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#connecting-using-the-default-authenticator),
you can get started quickly, but will soon find other options for authenticating
exist such as Single Sign-On (SSO), Multi-Factor Authentication (MFA),
and Key Pair Authentication.

If you routinely connect to Snowflake using Python, you're likely familiar with the
challenges of handling configurations, from hardcoding arguments in the
`snowflake.connector.connect()` function to dynamically loading configurations via
SnowSQL, and even juggling environment variables or JSON files. But guess what? There's
a simpler way!

With **dot-connect**, the hassle of managing credentials and configuration details is a
thing of the past. We've streamlined the process, making it more convenient and
efficient for you to connect to Snowflake from your Python code.

## Getting Started
#### Installing
Get started by installing **dot-connect** using
[pip](https://pypi.org/project/dot-connect) with the **snowflake** extra. It's just
one command away!

```bash
pip install "dot-connect[snowflake]"
```

#### Usage
Import the `dot-connect` module in your Python script and let it handle the connection
details for you.

```python
import dot_connect

con = dot_connect.snowflake.connect()
print(con.cursor().execute("SELECT 1;").fetchall())
```

## Look! An end-to-end demonstration.
We can't simply connect to Snowflake without showing how we can use it. Let's import
our modules and read a CSV from S3, save it, and load it into Snowflake.

###### To use Pandas to read the CSV from S3, s3fs needs to be installed.

```
>>> import dot_connect
>>> import pandas as pd

>>> df = pd.read_csv(
>>>     "s3://sfquickstarts/Summit 2022 Keynote Demo/campaign_spend/campaign_spend.csv"
>>> )
>>> df.to_csv("campaign_spend.csv", index=False)

>>> con = dot_connect.snowflake.connect()

>>> con.cursor().execute(
>>>     "CREATE OR REPLACE FILE FORMAT DOT_CONNECT TYPE = CSV SKIP_HEADER = 1;"
>>> ).fetchall()
>>> con.cursor().execute(
>>>     "CREATE OR REPLACE STAGE DOT_CONNECT FILE_FORMAT = DOT_CONNECT;"
>>> ).fetchall()
>>> con.cursor().execute(
>>>     "PUT file://campaign_spend.csv @DOT_CONNECT AUTO_COMPRESS=FALSE;"
>>> ).fetchall()

>>> df = con.cursor().execute(
>>>     """SELECT $1::VARCHAR(60) AS CAMPAIGN,
>>>               $2::VARCHAR(60) AS CHANNEL,
>>>               $3::DATE AS DATE,
>>>               $4::NUMBER(38, 0) AS TOTAL_CLICKS,
>>>               $5::NUMBER(38, 0) AS TOTAL_COST
>>>        FROM @DOT_CONNECT;"""
>>> ).fetch_pandas_all()

>>> df.head()

    CAMPAIGN                CHANNEL        DATE        TOTAL_CLICKS  TOTAL_COST
0   winter_sports           video          2012-06-03            21        1762
1   sports_across_cultures  video          2012-06-02            87         678
2   building_community      search_engine  2012-06-03            66         471
3   world_series            social_media   2017-12-28            72         591
4   winter_sports           email          2018-02-09           252        1841
```

## Conclusion
Just like that, we were able to query data in S3, load it into Snowflake, and query the
file in an internal stage using the Python connector.

Head on over to the docs section on the Snowflake [backend](../backends/snowflake.md)
to learn more.
