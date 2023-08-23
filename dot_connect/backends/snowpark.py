"""Utility module to handle Snowflake-related configurations."""
from dot_connect.backends import load_config


def connect(**kwargs):
    """
    Connect to Snowflake using Snowpark with environment variables.

    This function establishes a connection to a Snowflake database using the
    specified Snowpark connection parameters. It first loads a configuration
    dictionary containing default values and then updates it with any keyword
    arguments passed to the function. The resulting configuration is used to
    establish the Snowflake connection via Snowpark.

    More information regarding creating Snowpark sessions can be found at
    https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-session

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        snowflake.snowpark.Session: A session object representing the connection to the
        Snowflake database using Snowpark.

    Example:
        To connect to Snowflake using custom Snowpark parameters:
        >>> session = dot_connect.snowpark.connect(
        >>>     user='my_user',
        >>>     password='my_password')

    Note:
        This function requires the 'snowflake-snowpark-python' package to be
        installed. Make sure to have the package installed before using this
        function.

    """
    from snowflake.snowpark import Session

    config = load_config("SNOWFLAKE")

    config.update(**kwargs)

    return Session.builder.configs(config).create()
