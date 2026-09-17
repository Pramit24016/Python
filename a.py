import csv

# Define the filename
filename = "10_bit_binary_to_decimal.csv"

# Generate and write the 1024 rows
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow(["Binary", "Decimal"])
    
    # Loop from 0 to 1023
    for i in range(1024):
        # Format as a 10-digit binary string padded with leading zeros
        binary_str = f"{i:010b}"
        writer.writerow([binary_str, i])

print(f"Dataset successfully saved to {filename}")
