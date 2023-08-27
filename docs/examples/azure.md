---
hide:
  - toc
---

## Load Data from Azure Blob Storage into Pandas DataFrame

First, make sure you have the `azure-storage-blob` library installed. You can install it using pip:

```bash
pip install azure-storage-blob
```

```python
import pandas as pd
from io import BytesIO
from azure.storage.blob import BlobServiceClient

connection_string = 'your_connection_string_here'
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = 'your_container_name'
blob_name = 'your_blob_name.csv'

container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)
blob_data = blob_client.download_blob()

df = pd.read_csv(BytesIO(blob_data.readall()))
```

Remember to replace the placeholders (your_connection_string_here, your_container_name, and your_blob_name.csv) with your actual values.

Make sure you have your Azure Storage account connection string properly configured and secure before running this code.
