"""Utilities for working with private keys."""

import secrets
import string

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_random_password(length: int = 25) -> bytes:
    """Generate a random password of a given length.

    Args:
        length (int, optional): Length of the password. Defaults to 25.

    Returns:
        bytes: Random password.
    """
    return bytes(
        "".join(
            secrets.choice(string.ascii_letters + string.digits) for i in range(length)
        ),
        encoding="utf-8",
    )


def strip_public_key_headers(public_key: bytes) -> str:
    """
    Strip the headers and footers from a public key.

    Args:
        public_key (bytes): Public key to strip headers and footers from.

    Returns:
        str: Public key without headers and footers.
    """
    return "".join(public_key.decode("utf-8").split("\n")[1:-2])


def generate_key_pair(password: str) -> tuple:
    """
    Generate a key pair.

    Args:
        password (str): Password to encrypt the private key with.

    Returns:
        tuple: Tuple containing the encrypted private key and the public key.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    encrypted_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password),
    )
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return encrypted_private_key, public_key


def serialize_key(data: bytes, password: bytes) -> bytes:
    """
    Serialize a private key to DER format.

    Args:
        data (bytes): The private key in PEM format.
        password (bytes): The password to decrypt the private key.

    Returns:
        bytes: The private key in DER format.
    """
    p_key = serialization.load_pem_private_key(
        data,
        password,
        backend=default_backend(),
    )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return pkb


def create_aws_secret(client, secret_name: str, secret_binary: bytes):
    """
    Create an AWS Secrets Manager secret with the provided name and binary secret value.

    Args:
        secret_name (str): The name of the secret to be created or updated.
        secret_binary (bytes): The binary secret value to be stored in the secret.

    Raises:
        ClientError: If an error occurs while creating or updating the secret, such as a
        ResourceExistsException, it will be caught and handled.

    Notes:
        If a secret with the same name already exists, this function will update the
        existing secret with the new binary value.

    Example:
    create_aws_secret("my-secret", b"my-secret-value")
    """
    from botocore.exceptions import ClientError

    try:
        client.create_secret(Name=secret_name, SecretBinary=secret_binary)
    except ClientError as e:
        if e.response.get("Error").get("Code") == "ResourceExistsException":
            client.update_secret(SecretId=secret_name, SecretBinary=secret_binary)
