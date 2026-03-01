import imports as I
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CDC_PATH = os.path.join(BASE_DIR, 'data', 'parsed_data', 'cdc_parsed.csv')
POP_PATH = os.path.join(BASE_DIR, 'state_pops.csv')


def risk_factor(state_abbr: str):
    cancer_df = I.pd.read_csv(CDC_PATH)
    pop_df = I.pd.read_csv(POP_PATH)

    merged = I.pd.merge(
        cancer_df,
        pop_df,
        left_on='state',
        right_on='state_abbr'
    )

    state_df = merged[merged['state'] == state_abbr.upper()]

    if state_df.empty:
        raise ValueError(f"No data found for state '{state_abbr}'")

    rate = state_df['age_adjusted_cancer_rate'] * 1000
    total_cases = (rate * state_df['pop_100k']).sum()
    total_pop_100k = state_df['pop_100k'].sum()
    state_risk = total_cases / total_pop_100k

    rate_all = merged['age_adjusted_cancer_rate'] * 1000
    total_cases_all = (rate_all * merged['pop_100k']).sum()
    total_pop_all = merged['pop_100k'].sum()
    national_risk = total_cases_all / total_pop_all

    return state_risk, national_risk
