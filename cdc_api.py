# cdc_api.py

import sodapy

from config import get_client

DATASET_ID = "eav7-hnsx"

client = get_client(None)

results = client.get(DATASET_ID,limit=1000)

client.close()


