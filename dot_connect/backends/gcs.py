"""Utility module to download blobs from GCS buckets."""

from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """
    Download a blob from the bucket.

    Args:
        bucket_name (str): The name of the GCS bucket.
        source_blob_name (str): The path to the source blob to be downloaded.
        destination_file_name (str): The path on the local machine where the file should be saved.

    Example Usage:
        >>> bucket_name = 'YOUR_BUCKET_NAME'
        >>> source_blob_name = 'YOUR_SOURCE_BLOB_NAME'
        >>> destination_file_name = 'DESTINATION_PATH_ON_YOUR_LOCAL_MACHINE'
        >>> download_blob(bucket_name, source_blob_name, destination_file_name)
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)
