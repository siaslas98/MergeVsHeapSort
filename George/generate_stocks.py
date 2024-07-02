import csv
import random
import string

# Function to generate a random stock name
def generate_stock_name(length=5):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Function to generate a random stock price
def generate_stock_price(min_price=10, max_price=1000):
    return round(random.uniform(min_price, max_price), 2)

# Number of stocks to generate
num_stocks = 100000

# Specify the file name
filename = "stocks_100k.csv"

# Writing to csv file
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Stock Name', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for _ in range(num_stocks):
        stock_name = generate_stock_name()
        stock_price = generate_stock_price()
        writer.writerow({'Stock Name': stock_name, 'Price': stock_price})

print(f"CSV file '{filename}' with 100,000 stock names and prices created successfully.")
