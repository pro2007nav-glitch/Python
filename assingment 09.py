
import pandas as pd

# Read data from CSV file
data = pd.read_csv("input.csv")

# Convert CSV data to JSON format
json_data = data.to_json(orient="records", indent=4)

# Write JSON data to output file
with open("output.json", "w") as file:
    file.write(json_data)

print("CSV data converted to JSON successfully!")
