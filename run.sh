#!/bin/bash

# Parse arguments
day=$1
solution=$2
input=$3
expected_output=$4  # Optional 4th parameter

# Ensure that if the 4th parameter is provided, the 3rd must be 'e'
if [ -n "$expected_output" ] && [ "$input" != "e" ]; then
  echo "Error: The 4th parameter (expected output) can only be provided if the 3rd parameter is 'e' (example.txt)."
  exit 1
fi

# Map input shorthand to filenames
if [ "$input" == "e" ]; then
  input_file="example.txt"
else
  input_file="sample.txt"
fi

# Run the solution script and capture the output
output=$(python3 "day${day}/sol${solution}.py" < "day${day}/${input_file}")

# Print the output
echo "$output"

# Check if expected_output is provided and validate it
if [ -n "$expected_output" ]; then
  if [ "$output" == "$expected_output" ]; then
    echo "OK!"
  else
    echo "WRONG ANSWER. Expected $expected_output."
  fi
fi
