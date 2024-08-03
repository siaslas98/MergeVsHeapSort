import random
import string
from sorting import *

class Stock:
    def __init__(self, name, open, high, low, close, volume, openInt):
        self.name = name
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.openInt = openInt

    def __repr__(self):
        return f"Stock(name= {self.name}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, openInt={self.openInt})"

    @staticmethod
    def get_comparator(attribute, ascending=True):
        def comparator(stock):
            return getattr(stock, attribute) if ascending else -getattr(stock, attribute)
        return comparator


company_names = [
    "Apple", "Microsoft", "Amazon", "Google", "Facebook", "Tesla", "Alibaba", "Tencent", "Berkshire Hathaway",
    "Johnson & Johnson", "Samsung", "Visa", "Walmart", "Nestle", "Procter & Gamble", "Mastercard", "Disney",
    "PayPal", "Intel", "Nvidia", "ASML", "Coca-Cola", "Adobe", "Nike", "Salesforce", "Netflix", "Toyota", "PepsiCo",
    "Pfizer", "Cisco", "ExxonMobil", "AT&T", "Verizon", "Merck", "Qualcomm", "Chevron", "IBM", "Oracle", "Unilever",
    "McDonald's", "AbbVie", "Roche", "Novartis", "LVMH", "Amgen", "Costco", "Sony", "Bristol-Myers Squibb", "SAP",
    "Starbucks", "Philip Morris International", "Texas Instruments", "Gilead Sciences", "S&P Global", "3M", "Booking Holdings",
    "American Express", "Siemens", "Volkswagen", "Honeywell", "Schlumberger", "Colgate-Palmolive", "Bayer", "Lockheed Martin",
    "Charter Communications", "China Mobile", "Royal Dutch Shell", "Boeing", "General Electric", "UPS", "Total",
    "Anheuser-Busch", "Airbus", "Goldman Sachs", "Lowe's", "Target", "Morgan Stanley", "Deutsche Telekom", "GSK",
    "Anthem", "Medtronic", "SAP", "UBS", "Danone", "BBVA", "Enel", "AstraZeneca", "Siemens Healthineers", "Vodafone",
    "Rio Tinto", "Ericsson", "Heineken", "Stryker", "SABIC", "ABB", "WPP", "SK Hynix", "Kroger", "Sysco", "HP"
]

while len(company_names) < 100:
    company_names.extend(company_names)


# Function to generate random stock data
def generate_random_stock(name):
    open_price = round(random.uniform(100, 500), 2)
    high_price = round(random.uniform(open_price, open_price + 50), 2)
    low_price = round(random.uniform(open_price - 50, open_price), 2)
    close_price = round(random.uniform(low_price, high_price), 2)
    volume = random.randint(1000, 10000)
    openInt = random.randint(1000, 10000)
    return Stock(name, open_price, high_price, low_price, close_price, volume, openInt)


stock_list = [generate_random_stock(company_names[i]) for i in range(100)]


# Setup sort_info
class SortInfo:
    def __init__(self, stock_list):
        self.list = stock_list


sort_info = SortInfo(stock_list)


# Define screen and clock (for illustration purposes, not used in this example)
screen = None
clock = None

# Perform heap sort based on the 'close' attribute
comparator = Stock.get_comparator('close', ascending=True)
# heap_sort(screen, clock, sort_info, comparator)
timsort(screen, sort_info, comparator)

# Display the generated stock objects
for i in range(n-1):
    print(stock_list[i].close)
    if stock_list[i].close > stock_list[i+1].close:
        print("Not in order")
        break
