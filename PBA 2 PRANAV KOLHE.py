
import re

# Read text from a document
with open("document.txt", "r") as file:
    text = file.read()

# Regex pattern for Indian mobile numbers
pattern = r'(?<!\d)(?:\+91[\s-]?|91[\s-]?|0)?[6-9]\d{9}(?!\d)'

# Extract mobile numbers
numbers = re.findall(pattern, text)

# Display the extracted numbers
print("Valid Indian Mobile Numbers:")
for number in numbers:
    print(number)

if not numbers:
    print("No valid mobile numbers found.")