"""Utility module to handle AWS service-related configurations."""

import boto3

from dot_connect.backends import load_config


def connect(service_name, **kwargs):
    r"""
    Connect to an AWS service using boto3 with environment variables.

    This function establishes a connection to an AWS service using the specified
    connection parameters. It first loads a configuration dictionary containing
    default values and then updates it with any keyword arguments passed to the
    function. The resulting configuration is used to establish the AWS service connection.

    The AWS SDK, `boto3`, follows a hierarchy to authenticate:

    1. Environment Variables: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
    2. AWS Configuration Files: ~/.aws/credentials (or %UserProfile%\.aws\credentials on Windows).
    3. AWS CLI: Configuration set via `aws configure`.

    Args:
        service_name (str): The name of the AWS service to connect to (e.g., 's3', 'ec2').
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        boto3.Session.resource or boto3.Session.client: A connection object representing
        the connection to the AWS service.

    Example:
        To connect to S3 using custom parameters:
        >>> s3_resource = connect('s3',
        >>>                       aws_access_key_id='YOUR_ACCESS_KEY',
        >>>                       aws_secret_access_key='YOUR_SECRET_KEY',
        >>>                       region_name='YOUR_REGION',
        >>> )

    Note:
        This function requires the 'boto3' package to be installed.
        Make sure to have the package installed before using this function.
    """
    config = load_config("AWS")

    config.update(**kwargs)

    return boto3.client(service_name, **kwargs)
