# download_eia.py
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from eia_api import get_eia
from config import EIA_API_KEY

RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

df_co2 = get_eia(start_year=2022, end_year=2022, api_key=EIA_API_KEY)

csv_path = os.path.join(RAW_DATA_DIR, "eia_data.csv")
df_co2.to_csv(csv_path, index=False)
print(f"Saved CO2 emissions data to {csv_path}")
