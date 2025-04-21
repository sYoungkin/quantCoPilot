
import pandas as pd



def onboard_data(pair="EURUSD", interval="1m", asset_type="forex"):

    
    # Read data
    DATA_PATH = f"data/{pair}_{interval}.csv"
    df = pd.read_csv(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)

    # Drop N/As
    df = df.dropna()
    


    return df