import pandas as pd
import csv
import sys
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from cdc_api import get_client, DATASET_ID

RAW_DATA_DIR = "data/raw_data"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

csv_path = os.path.join(RAW_DATA_DIR, "cdc_data.csv")
offset_path = os.path.join(RAW_DATA_DIR, "offset.txt")

client = get_client(None)

batch_size = 1000

if os.path.exists(offset_path):
    with open(offset_path, "r") as f:
        offset = int(f.read().strip())
    first_batch = False
    print(f"Resuming from offset {offset}")
else:
    offset = 0
    first_batch = True

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = None

    while True:
        try:
            batch = client.get(DATASET_ID, limit=batch_size, offset=offset)
        except Exception as e:
            print(f"Error fetching batch at offset {offset}: {e}")
            time.sleep(5)
            continue

        if not batch:
            print("No more data to fetch.")
            break

        if first_batch:
            writer = csv.DictWriter(f, fieldnames=batch[0].keys())
            writer.writeheader()
            first_batch = False
        elif writer is None:
            writer = csv.DictWriter(f, fieldnames=batch[0].keys())

        writer.writerows(batch)
        f.flush()

        offset += batch_size

        with open(offset_path, "w") as off:
            off.write(str(offset))

        print(f"Fetched {offset} rows...")

client.close()
print(f"CDC data saved to {csv_path}")
print("Download complete!")
