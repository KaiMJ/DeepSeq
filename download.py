import pandas as pd
import requests
import json
import os
from urllib.error import HTTPError


def download_crypto_data(ticker, exchange, start_year, end_year, data_dir='data'):
    for d in range(start_year, end_year + 1):

        url = f"https://www.cryptodatadownload.com/cdd/{exchange}_{ticker}USD_{d}_minute.csv"
        print(url)

        try:
            filename = os.path.join(data_dir, ticker, f'{d}_minute.csv')
            if os.path.exists(filename):
                print(f'Skipping {filename} because it already exists')
                continue

            os.makedirs(data_dir, exist_ok=True)
            os.makedirs(os.path.join(data_dir, ticker), exist_ok=True)

            df = pd.read_csv(url, skiprows=1)
            if d == end_year:  # let's limit to 3/19 Wednsday.
                df = df[df['Date'] <= '2025-03-19 00:00:00']

            df.to_csv(filename, index=False)

            print(f'Downloaded {filename}')
        except HTTPError as e:
            print(f'Error downloading {url}: {e}')


if __name__ == '__main__':
    # currently 2025 errors for both Gemini and Bitstamp.
    # we may add it later if it gets fixed.
    download_crypto_data('BTC', 'Gemini', 2015, 2025)
    download_crypto_data('ETH', 'Bitstamp', 2017, 2025)
    download_crypto_data('XRP', 'Bitstamp', 2016, 2025)
    download_crypto_data('ADA', 'Bitstamp', 2022, 2025)
    download_crypto_data('SOL', 'Gemini', 2022, 2025)
