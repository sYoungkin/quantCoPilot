import argparse
import yfinance as yf


def fetch_data(pair="EURUSD", interval="1m", period="1d"):
    pair = f"{pair}=X"
    ticker = yf.Ticker(pair)
    df = ticker.history(interval=interval, period=period)
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError(f"No data returned for {pair} with interval '{interval}' and period '{period}'")

    # Convert index to UTC and drop timezone
    df.index = df.index.tz_convert("UTC").tz_localize(None)

    # Keep only price columns
    df = df[["Open", "High", "Low", "Close"]]

    # Lowercase column names
    df.columns = [col.lower() for col in df.columns]

    # Rename index to 'timestamp' and reset it to be a column
    df.index.name = "timestamp"
    df = df.reset_index()

    # Save pdf
    symbol = pair.replace("=X", "")
    filename = f"data/{symbol}_{interval}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved: {filename}")

    return df

# === Example Usage with Arguments ===
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch Twelve Data OHLCV data and save as CSV.')
    parser.add_argument('--pair', type=str, default='EURUSD', help='e.g. BTCUSD, ETHUSD')
    parser.add_argument('--timeframe', type=str, default='1m', help='e.g. 1m, 5m, 1h, 1d')
    parser.add_argument('--period', type=str, default=100, help='Number of candles to fetch')
    args = parser.parse_args()

    fetch_data(pair=args.pair, interval=args.timeframe, period=args.period)