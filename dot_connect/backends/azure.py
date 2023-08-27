"""Utility module to handle Azure Blob Storage service-related configurations."""

from azure.storage.blob import BlobServiceClient

from dot_connect.backends import load_config


def connect_blob_service(**kwargs):
    """
    Connect to Azure Blob Storage using the environment variables.

    This function establishes a connection to Azure Blob Storage using the specified
    connection parameters. It first loads a configuration dictionary containing
    default values and then updates it with any keyword arguments passed to the
    function. The resulting configuration is used to establish the Blob service connection.

    Args:
        **kwargs: Additional keyword arguments to customize the connection
                  parameters. These arguments will be used to update the default
                  configuration.

    Returns:
        azure.storage.blob.BlobServiceClient: A client object representing the
        connection to the Azure Blob Storage.

    Example:
        To connect to Azure Blob Storage using a custom connection string:
        >>> blob_service_client = connect_blob_service(connection_string='YOUR_CONNECTION_STRING')

    Note:
        This function requires the 'azure-storage-blob' package to be installed.
        Make sure to have the package installed before using this function.

    """
    config = load_config("AZURE_BLOB_STORAGE")

    config.update(**kwargs)

    return BlobServiceClient(**config)
