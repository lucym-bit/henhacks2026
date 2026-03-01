# config.py
import os
import pandas as pd
from sodapy import Socrata

EIA_URL = "https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/"
EIA_API_KEY = os.getenv("EIA_API_KEY")

if EIA_API_KEY is None:
    raise RuntimeError("EIA_API_KEY not set in environment")

CDC_DOMAIN = "data.cdc.gov"
DATASET_ID = "eav7-hnsx"

<<<<<<< Updated upstream
def get_client(app_token, username=None, password=None):
    return Socrata(CDC_DOMAIN,
                 app_token,
                 username=username,
                 password=password)
=======
def get_client(app_token):
    return Socrata(CDC_DOMAIN, None)
>>>>>>> Stashed changes
