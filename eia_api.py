# eia_api.py
import requests
from config import EIA_BASE_URL, EIA_API_KEY

def get_eia(endpoint, params=None):
    params = params or {}
    params["api_key"] = EIA_API_KEY

    url = f"{EIA_BASE_URL}/{endpoint}"
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()
