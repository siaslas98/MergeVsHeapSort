import pygame as pg
from constants import *
from images import *
import csv
import random
import pandas as pd
import yfinance as yf

class Stocks: 
    def __init__(self):
        self.stocklist = []
        self.stock_symbols = []
    
    def Generate_Stock_for_day(self, number, date):
        nasdaq_symbols = [
        "AAPL", "GOOGL", "MSFT", "AMZN", "FB", "NVDA", "TSLA", "BRK-B", "JPM", "UNH",
        "V", "JNJ", "WMT", "PG", "XOM", "CVX", "BAC", "DIS", "HD", "MA",
        "KO", "PEP", "CRM", "INTC", "ADBE", "CSCO", "NFLX", "COST", "CMCSA", "TXN",
        "PYPL", "PEP", "MCD", "NKE", "MCD", "UNP", "UPS", "CAT", "IBM", "ORCL",
        "CRM", "QCOM", "AMD", "TXN", "INTU", "ADP", "LOW", "SBUX", "DHR", "HON",
        "BA", "LMT", "RTX", "UNH", "CVS", "MRK", "PFE", "ABT", "LLY", "GILD",
        "AMGN", "TMO", "AZN", "NVO", "BMY", "MRNA", "REGN", "ILMN", "CELG", "BIIB",
        "VRTX", "INCY", "SGEN", "ALXN", "REGN", "ANTM", "HUM", "Cigna", "AET", "DVA",
        "DGX", "BDX", "SYK", "EW", "CI", "TGT", "TJX", "DLTR", "DG", "WBA",
        "AAPL", "GOOGL", "MSFT", "AMZN", "FB", "NVDA", "TSLA", "BRK-B", "JPM", "UNH",
        "V", "JNJ", "WMT", "PG", "XOM", "CVX", "BAC", "DIS", "HD", "MA",
        "KO", "PEP", "CRM", "INTC", "ADBE", "CSCO", "NFLX", "COST", "CMCSA", "TXN",
        "PYPL", "PEP", "MCD", "NKE", "MCD", "UNP", "UPS", "CAT", "IBM", "ORCL",
        "CRM", "QCOM", "AMD", "TXN", "INTU", "ADP", "LOW", "SBUX", "DHR", "HON",
        "BA", "LMT", "RTX", "UNH", "CVS", "MRK", "PFE", "ABT", "LLY", "GILD",
        "AMGN", "TMO", "AZN", "NVO", "BMY", "MRNA", "REGN", "ILMN", "CELG", "BIIB",
        "VRTX", "INCY", "SGEN", "ALXN", "REGN", "ANTM", "HUM", "Cigna", "AET", "DVA",
        "DGX", "BDX", "SYK", "EW", "CI", "TGT", "TJX", "DLTR", "DG", "WBA",
        "AAPL", "GOOGL", "MSFT", "AMZN", "FB", "NVDA", "TSLA", "BRK-B", "JPM", "UNH",
        "V", "JNJ", "WMT", "PG", "XOM", "CVX", "BAC", "DIS", "HD", "MA",
        "KO", "PEP", "CRM", "INTC", "ADBE", "CSCO", "NFLX", "COST", "CMCSA", "TXN",
        "PYPL", "PEP", "MCD", "NKE", "MCD", "UNP", "UPS", "CAT", "IBM", "ORCL",
        "CRM", "QCOM", "AMD", "TXN", "INTU", "ADP", "LOW", "SBUX", "DHR", "HON",
        "BA", "LMT", "RTX", "UNH", "CVS", "MRK", "PFE", "ABT", "LLY", "GILD",
        "AMGN", "TMO", "AZN", "NVO", "BMY", "MRNA", "REGN", "ILMN", "CELG", "BIIB",
        "VRTX", "INCY", "SGEN", "ALXN", "REGN", "ANTM", "HUM", "Cigna", "AET", "DVA",
        "DGX", "BDX", "SYK", "EW", "CI", "TGT", "TJX", "DLTR", "DG", "WBA"
        ]

        # Get the stock symbols
        self.stock_symbols = nasdaq_symbols

        # Generate stock data
        for i in range(number):
            symbol = self.stock_symbols[i]
            stock = {
                "Stock_name": symbol,
                "Stock_price": round(random.uniform(min_range, max_range), 2),
                "Stock_market_Cap": round(random.uniform(min_range, max_range), 2),
                "Stock_52_week_low": round(random.uniform(min_range, max_range), 2),
                "Stock_52_week_high": round(random.uniform(min_range, max_range), 2),
            }
            self.stocklist.append(stock)

    def get_stocklist(self):
        return self.stocklist
    
    def get_stock_price_by_symbol(self, symbol):
        for stock in self.stocklist:
            if stock["Stock_name"] == symbol:
                return stock["Stock_price"]
        return None  # Return None if the symbol is not found
    
    def get_all_stock_market_caps(self):
        stock_market_caps = [stock["Stock_market_Cap"] for stock in self.stocklist]
        return stock_market_caps

    def get_all_stock_52_week_low(self):
        stock_52_week_low = [stock["Stock_52_week_low"] for stock in self.stocklist]
        return stock_52_week_low

    def get_all_stock_52_week_high(self):
        stock_52_week_high = [stock["Stock_52_week_high"] for stock in self.stocklist]
        return stock_52_week_high




        

        