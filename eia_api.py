# eia_api.py
import pandas as pd
import requests
from config import EIA_URL, EIA_API_KEY

def get_eia(start_year, end_year, api_key):
    params = {
	"api_key": api_key,
        "frequency": "annual",
       	"data": ["value"],
    	"facets[sectorId][]": "TT",
	"start": start_year,
    	"end": end_year,
       	"offset": 0,
       	"length": 5000
    }
    all_rows = []
    url = EIA_URL

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()["response"]["data"]
    return pd.DataFrame(data)
