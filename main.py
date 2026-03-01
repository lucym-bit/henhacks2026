import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CDC_PATH = os.path.join(BASE_DIR, 'data', 'parsed_data', 'cdc_parsed.csv')
POP_PATH = os.path.join(BASE_DIR, 'data', 'parsed_data', 'state_pops.csv')


def risk_factor(state_abbr: str) -> float:
    cancer_df = pd.read_csv(CDC_PATH)
    pop_df = pd.read_csv(POP_PATH)

    merged = pd.merge(cancer_df, pop_df, on='stateabbr')
    merged.rename(columns={'population_x': 'cdc_population', 'population_y': 'state_population'}, inplace=True)

    state_df = merged[merged['stateabbr'].str.upper() == state_abbr.upper()]

    if state_df.empty:
        raise ValueError(f"No data found for state '{state_abbr}'")

    total_cases = (state_df['age_adjusted_cancer_rate'] * state_df['state_population']).sum()
    total_pop = state_df['state_population'].sum()

    return total_cases / total_pop


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        state = sys.argv[1]
    else:
        state = input("Enter state abbreviation (e.g., PA): ").strip().upper()

    try:
        result = risk_factor(state)
        print(f"{result:.2f}")
    except ValueError as e:
        print(e)
