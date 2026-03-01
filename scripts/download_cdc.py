import pandas as pd
import csv
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from cdc_api import get_client, DATASET_ID

RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

csv_path = os.path.join(RAW_DATA_DIR, "cdc_data.csv")

client = get_client(None)

offset = 0
batch_size = 5000
first_batch = True

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = None

    while True:
        batch = client.get(DATASET_ID, limit=batch_size, offset=offset)

        if not batch:
            break

        if first_batch:
            writer = csv.DictWriter(f, fieldnames=batch[0].keys())
            writer.writeheader()
            first_batch = False

        writer.writerows(batch)

        offset += batch_size
        print(f"Fetched {offset} rows...")

client.close()
print(f"CDC data saved to {csv_path}")
print("Download complete!")
