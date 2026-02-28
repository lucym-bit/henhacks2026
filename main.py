# main.py

from eia_api import get_eia
import imports as I

data = get_eia(
    "electricity/rto/region-data/data",
    params={
        "frequency": "hourly",
        "data[0]": "value",
        "facets[type][]": "D",          # Demand
        "facets[respondent][]": "PJM",  # subregion
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "length": 24                    # last 24 hours
    }
)

rows = data["response"]["data"]

df = I.pd.DataFrame(rows)
df["period"] = I.pd.to_datetime(df["period"])
df = df.sort_values("period")

I.plt.figure(figsize=(10, 5))
I.plt.plot(df["period"], df["value"])
I.plt.xlabel("Time")
I.plt.ylabel("Demand (MW)")
I.plt.tight_layout()

for region, g in df.groupby("respondent"):
    I.plt.plot(g["period"], g["value"], label=region)

I.plt.legend()
I.plt.title("Hourly Electricity Demand by Subregion")
I.plt.savefig("pjm_hourly_demand.png", dpi=200)
I.plt.show()
