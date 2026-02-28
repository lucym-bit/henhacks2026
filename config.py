# config.py
import os
import pandas as pd
from sodapy import Socrata

EIA_BASE_URL = "https://api.eia.gov/v2"
EIA_API_KEY = os.getenv("EIA_API_KEY")

if EIA_API_KEY is None:
    raise RuntimeError("EIA_API_KEY not set in environment")

CDC_DOMAIN = "data.cdc.gov"
DATASET_ID = "eav7-hnsx"

def get_client(app_token, username=None, password=None):
    return Socrata(CDC_DOMAIN,
                 app_token,
                 username=username,
                 password=password)
