---
hide:
  - toc
---

# AWS
With **dot-connect**, the hassle of managing credentials and configuration details is a
thing of the past. We've streamlined the process, making it more convenient and
efficient for you to connect to AWS from your Python code.

## Getting Started
#### Installing
Get started by installing **dot-connect** using
[pip](https://pypi.org/project/dot-connect) with the **aws** extra. It's just one
command away!

```bash
pip install "dot-connect[aws]"
```

### download CSV from S3 -> sort data -> to Parquet -> upload to S3

```python
import dot_connect
from io import BytesIO
import pandas as pd
import gzip

s3 = dot_connect.aws.connect("s3")

response = s3.get_object(Bucket="twhite-dc", Key="penguins.csv.gz")
data = response["Body"].read()
data = gzip.decompress(data)
df = pd.read_csv(BytesIO(data))

df = pd.read_csv("s3://twhite-dc/penguins.csv.gz")

df = df.sort_values(by=["year", "species"])
df.to_parquet("penguins.parquet.snappy", compression="snappy", index=False)

s3.upload_file("penguins.parquet.snappy", "twhite-dc", "penguins.parquet.snappy")
```
