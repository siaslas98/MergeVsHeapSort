import random
import string
from sorting import *
import os
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


company_names = []
directory = 'Stocks/'
for filename in os.listdir(directory):
    stock_name = filename.split('.')[0].upper()
    company_names.append(stock_name)

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
    test_run_timsort = sort_info
    timer_1.start()
    heap_sort(sort_info, comparator)
    timer_1.stop()
    sort_info.heap_timer = timer_1.get_value()
    timer_2.start()
    timsort(test_run_timsort, comparator)
    timer_2.stop()
    sort_info.timsort_timer = timer_2.get_value()


def handle_descending(sort_info):
    sort_info.list.reverse()


def set_top_5(attribute, sort_info, order):
    reverse_after = False
    if order == "Ascending":
        sort_info.list.reverse()
        reverse_after = True
    if order == "Descending":
        sort_info.list.reverse()
        reverse_after = True
    for stock in range(0, 5):
        sort_info.top_5[stock] = (sort_info.list[stock].name, get_attribute(attribute, sort_info, stock))
    if reverse_after:
        sort_info.list.reverse()


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
