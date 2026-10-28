
from pathlib import Path

# Create the input file in the same folder as this program
folder = Path(__file__).resolve().parent
input_file = folder / "input.txt"

# Read the input file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two_lines = lines[:2]

# Write them into a new file
output_file = folder / "output.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(first_two_lines)

print("First two lines saved successfully!")
