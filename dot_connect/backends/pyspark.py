"""Utility module to handle PySpark-related configurations."""

from pyspark.sql import SparkSession

from dot_connect.backends import load_config


def connect(**kwargs):
    """
    Connect to Spark using the environment variables.

    This function establishes a connection using the specified
    connection parameters. It first loads a configuration dictionary containing
    default values and then updates it with any keyword arguments passed to the
    function. The resulting configuration is used to establish the SparkSession
    connection.

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        pyspark.sql.SparkSession: A SparkSession object representing the
        connection.

    Example:
        To connect using custom parameters:
        >>> spark = connect(appName="MyApp", master="local[*]")

    Note:
        This function requires the 'pyspark' and 'delta' packages to be
        installed. Make sure to have the packages installed before using this
        function.

    """
    # TODO: What's a good default name?
    config = load_config("PYSPARK")

    config.update(**kwargs)

    return (
        SparkSession.builder.appName(config.get("appName", "MyApp"))
        .master(config.get("master", "local"))
        .getOrCreate()
    )
