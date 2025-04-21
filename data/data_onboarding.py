
import pandas as pd


def onboard_data(pair="EUR/USD", interval="1min", asset_type="forex"):

    
    # read data
    symbol = pair.replace("/", "")
    DATA_PATH = f"data/{symbol}_{interval}.csv"
    df = pd.read_csv(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
    df = df.sort_values('timestamp')

    print(df[['timestamp']].head())
    print(df[['timestamp']].tail())

    #print(len(df))

    # remove_weekend_gaps
    # if asset_type == "forex":
    #     df['weekday'] = df['timestamp'].dt.weekday
    #     df['hour'] = df['timestamp'].dt.hour

    #     df['date'] = df['timestamp'].dt.date
    #     print(df.groupby('date').size())

    #     # Remove entire weekend (Fri 21:00 UTC to Sun 21:00 UTC)
    #     mask = ~(
    #         ((df['weekday'] == 4) & (df['hour'] >= 21)) |  # Friday after 21:00
    #         (df['weekday'] == 5) |                         # All of Saturday
    #         ((df['weekday'] == 6) & (df['hour'] < 21))     # Sunday before 21:00
    #     )
    #     df = df[mask].copy()

    #     df = df[mask].copy()
    #     print("Filtered:")
    #     print(df.groupby('date').size())
    # #print(df.head(100))
    # #print(df.tail(100))
    # print(f"✅ Loaded {len(df)} rows for {pair} ({interval}) after weekend filtering.")


    return df