#!/usr/bin/env bash
set -euo pipefail

INPUT="data/raw_data/eia_data.csv"
OUTPUT="data/parsed_data/eia_parsed.csv"

mkdir -p data/parsed_data

echo "state,co2_emissions" > "$OUTPUT"

declare -A STATES=(
  ["Alabama"]="AL" ["Alaska"]="AK" ["Arizona"]="AZ" ["Arkansas"]="AR"
  ["California"]="CA" ["Colorado"]="CO" ["Connecticut"]="CT" ["Delaware"]="DE"
  ["Florida"]="FL" ["Georgia"]="GA" ["Hawaii"]="HI" ["Idaho"]="ID"
  ["Illinois"]="IL" ["Indiana"]="IN" ["Iowa"]="IA" ["Kansas"]="KS"
  ["Kentucky"]="KY" ["Louisiana"]="LA" ["Maine"]="ME" ["Maryland"]="MD"
  ["Massachusetts"]="MA" ["Michigan"]="MI" ["Minnesota"]="MN"
  ["Mississippi"]="MS" ["Missouri"]="MO" ["Montana"]="MT" ["Nebraska"]="NE"
  ["Nevada"]="NV" ["New Hampshire"]="NH" ["New Jersey"]="NJ"
  ["New Mexico"]="NM" ["New York"]="NY" ["North Carolina"]="NC"
  ["North Dakota"]="ND" ["Ohio"]="OH" ["Oklahoma"]="OK" ["Oregon"]="OR"
  ["Pennsylvania"]="PA" ["Rhode Island"]="RI" ["South Carolina"]="SC"
  ["South Dakota"]="SD" ["Tennessee"]="TN" ["Texas"]="TX" ["Utah"]="UT"
  ["Vermont"]="VT" ["Virginia"]="VA" ["Washington"]="WA"
  ["West Virginia"]="WV" ["Wisconsin"]="WI" ["Wyoming"]="WY"
)


echo "state,co2_emissions" > "$OUTPUT"

tail -n +2 "$INPUT" | awk -F',' '{
  state=$6
  co2=$2
  if (state!="" && co2!="") print state "," co2
}' >> "$OUTPUT"

echo "✓ Parsed EIA data written to $OUTPUT"
