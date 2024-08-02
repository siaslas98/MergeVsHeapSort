import pandas as pd
import os
import logging
from stock import Stock

# Set up logging
logging.basicConfig(filename='load_data.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_file(file_path, selected_date):
    """Load a file and filter by the selected date"""
    try:
        df = pd.read_csv(file_path)
        filtered_df = df[df['Date'] == selected_date]
        if not filtered_df.empty:
            return filtered_df
        else:
            logging.info(f"No data found for {selected_date} in {file_path}")
            return None
    except pd.errors.EmptyDataError:
        logging.info(f"Empty file: {file_path}")
        return None
    except pd.errors.ParserError:
        logging.info(f"Parsing error in file: {file_path}")
        return None
    except Exception as e:
        logging.info(f"Error loading {file_path}: {e}")
        return None


def get_file_paths(directory, extension=".csv"):
    """Return a list of file paths with the given extension in the specified directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]


def load_data(date, directory):
    """Load data for the given date from files in the specified directory."""
    file_paths = get_file_paths(directory, ".csv")
    stock_data = []

    for file_path in file_paths:
        data = load_file(file_path, date)
        if data is not None:
            for _, row in data.iterrows():
                stock_data.append(Stock(row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['OpenInt']))

    return stock_data


