# config.py
import os
import pandas as pd
from sodapy import Socrata

EIA_BASE_URL = "https://api.eia.gov/v2"
EIA_API_KEY = os.getenv("EIA_API_KEY")

if EIA_API_KEY is None:
    raise RuntimeError("EIA_API_KEY not set in environment")

client = Socrata("data.cdc.gov",
	MyAppToken,
	username="winslow@udel.edu",
	password="!xPanTNmm7ShDut")
