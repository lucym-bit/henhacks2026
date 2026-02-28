# cdc_api.py

import sodapy

from config import get_client

DATASET_ID = "eav7-hnsx"
APP_TOKEN = "CDC_APP_TOKEN"
USERNAME = "winslow@udel.edu"
PASSWORD = "!xPanTNmm7ShDut"

client = get_client("APP_TOKEN","USERNAME","PASSWORD")

results = client.get(DATASET_ID,limit=1000)

client.close()


