# main.py

import pandas as pd
import os

cancer_df = pd.read_csv('data/parsed_data/cdc_parsed.csv')
pop_df = pd.read_csv('state_pops.csv')
merged = pd.merge(cancer_df, pop_df, left_on='state', right_on='state_abbr')
merged['cancer_rate_per_100k'] = merged['age_adjusted_cancer_rate'] * 1000
merged['impact_count'] = merged['cancer_rate_per_100k'] * merged['pop_100k']

total_us_cases = (merged['cancer_rate_per_100k'] * merged['pop_100k']).sum()
total_us_pop_100k = merged['pop_100k'].sum()
national_avg_rate = total_us_cases / total_us_pop_100k
print(f"--- NATIONAL STATISTICS ---") 
print(f"Total US Population (Est): {total_us_pop_100k * 100000:,.0f}") 
print(f"National Cancer Rate: {national_avg_rate:.2f} per 100,000")

merged.to_csv('final_normalized_data.csv', index=False)
print("Normalization complete! Saved to final_normalized_data.csv")



