#!/usr/bin/env bash
set -euo pipefail

RAW="data/raw_data/cdc_data.csv"
PARS="data/parsed_data"
mkdir -p "$PARS"

SEMIPARSED="$PARS/semiparsed_cdc.csv"
FINAL="$PARS/cdc_parsed.csv"
STATE_POP="$PARS/state_populations.csv"

echo "state,area,age_adjusted_cancer_rate,population" > "$SEMIPARSED"

tail -n +2 "$RAW" | awk -F',' '
BEGIN { OFS="," }
{
  question = tolower($20)
  if (question ~ /cancer/ && question !~ /screening/) {
    if ($10 != "" && $12 != "") {
      print $2,$4,$10,$12
    }
  }
}' >> "$SEMIPARSED"

echo "state,age_adjusted_cancer_rate,population" > "$FINAL"

tail -n +2 "$SEMIPARSED" | awk -F',' '
{
  state=$1
  rate[state]+=$3
  count[state]++
  if ($4>pop[state]) pop[state]=$4
}
END {
  OFS=","
  for (s in rate) {
    print s, rate[s]/count[s], pop[s]
  }
}' >> "$FINAL"

echo "state,population" > "$STATE_POP"
tail -n +2 "$FINAL" | awk -F',' '{print $1","$3}' >> "$STATE_POP"

echo "All CDC parsing complete!"
