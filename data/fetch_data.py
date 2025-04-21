# fetch_data.py — Pull OHLCV data from Twelve Data and save to CSV

import requests
import pandas as pd
from datetime import datetime
import argparse
from dotenv import load_dotenv
import os
load_dotenv(override=True)


# === CONFIG ===
API_KEY = os.getenv('TD_API_KEY')
BASE_URL = "https://api.twelvedata.com/time_series"

# === FUNCTION ===
def fetch_data(pair="EUR/USD", interval="1min", limit=100):
    #symbol = pair.replace("/", "")  # Twelve Data uses EURUSD format
    params = {
        "symbol": pair,
        "interval": interval,
        "outputsize": limit,
        "apikey": API_KEY,
        "format": "JSON"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "values" not in data:
        raise ValueError(f"Error fetching data: {data.get('message', 'No data returned')}")

    df = pd.DataFrame(data["values"])
    df = df.rename(columns={"datetime": "timestamp"})
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    # Convert numeric columns
    for col in ["open", "high", "low", "close"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    symbol = pair.replace("/", "")
    filename = f"data/{symbol}_{interval}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved: {filename}")



    return df

# === Example Usage with Arguments ===
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch Twelve Data OHLCV data and save as CSV.')
    parser.add_argument('--pair', type=str, default='EUR/USD', help='e.g. BTC/USD, ETH/USD')
    parser.add_argument('--timeframe', type=str, default='1min', help='e.g. 1min, 5min, 1h, 1day')
    parser.add_argument('--limit', type=int, default=100, help='Number of candles to fetch')
    args = parser.parse_args()

    fetch_data(pair=args.pair, interval=args.timeframe, limit=args.limit)
