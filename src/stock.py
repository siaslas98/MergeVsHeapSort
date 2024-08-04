import random
import string
from sorting import *
from timer import *
from constants import *

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

while len(company_names) < n:
    company_names.extend(company_names)


# Function to generate random stock data
def generate_random_stock(name):
    open_price = round(random.uniform(min_range, max_range), 2)
    high_price = round(random.uniform(min_range, max_range), 2)
    low_price = round(random.uniform(min_range, max_range), 2)
    close_price = round(random.uniform(min_range, max_range), 2)
    volume = random.randint(min_range, max_range)
    openInt = random.randint(min_range, max_range)
    return Stock(name, open_price, high_price, low_price, close_price, volume, openInt)


def sort_helper(sort_info, attribute):
    comparator = Stock.get_comparator(attribute)
    timer_1.start()
    print("Timer 1 Started")
    heap_sort(sort_info, comparator)
    timer_1.stop()
    sort_info.heap_timer = timer_1.get_value()
    timer_1.reset()
    timer_2.start()
    print("Timer 2 Started")
    timsort(sort_info, comparator)
    timer_2.stop()
    sort_info.timsort_timer = timer_2.get_value()
    timer_2.reset()
    print(f"Heap Sort: {sort_info.heap_timer}")
    print(f"TimSort: {sort_info.timsort_timer}")


def handle_descending(sort_info):
    sort_info.list.reverse()


def set_top_5(attribute, sort_info):
<<<<<<< Updated upstream
    if sort_info.selected_order == "Ascending":
        for i in range(0, 5):
            sort_info.top_5[i] = (sort_info.list[n-i-1].name, get_attribute(attribute, sort_info, n-i-1))
    else:
        for i in range(0, 5):
            sort_info.top_5[i] = (sort_info.list[i].name, get_attribute(attribute, sort_info, i))
=======
    for stock in range(0, 5):
        sort_info.top_5[stock] = (sort_info.list[stock].name, get_attribute(attribute, sort_info, n-1-stock))
>>>>>>> Stashed changes


def get_attribute(attribute, sort_info, n):
    if attribute == "Open":
        return sort_info.list[n].open
    elif attribute == "High":
        return sort_info.list[n].high
    elif attribute == "Low":
        return sort_info.list[n].low
    elif attribute == "Close":
        return sort_info.list[n].close
    elif attribute == "Volume":
        return sort_info.list[n].volume
    elif attribute == "OpenInt":
        return sort_info.list[n].openInt


def sort_off_attribute(attribute, sort_info):
    if attribute == "Open":
        sort_helper(sort_info, 'open')
    elif attribute == "High":
        sort_helper(sort_info, 'high')
    elif attribute == "Low":
        sort_helper(sort_info, 'low')
    elif attribute == "Close":
        sort_helper(sort_info, 'close')
    elif attribute == "Volume":
        sort_helper(sort_info, 'volume')
    elif attribute == "OpenInt":
        sort_helper(sort_info, 'openInt')
