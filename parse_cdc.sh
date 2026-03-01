#!/usr/bin/env bash
set -euo pipefail

RAW="data/raw_data/cdc_data.csv"
PROC="data/parsed_data"
mkdir -p "$PROC"

SEMIPARSED="$PROC/semiparsed_cdc.csv"
FINAL="$PROC/cdc_parsed.csv"
STATE_POP="$PROC/state_populations.csv"

csvcut -c stateabbr,locationname,data_value,totalpopulation,short_question_text "$RAW" \
  | csvgrep -c short_question_text -r "cancer" \
  | csvgrep -c short_question_text -v -r "screening" \
  > "$SEMIPARSED"

csvcut -c stateabbr,data_value,totalpopulation "$SEMIPARSED" \
  | csvstat --mean data_value --sum totalpopulation \
  > "$FINAL"

csvcut -c stateabbr,totalpopulation "$FINAL" > "$STATE_POP"

echo "CDC parsing complete!"
