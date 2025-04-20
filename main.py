import pandas as pd
from datetime import datetime
import argparse
from indicators.ema_crossover import ema_crossover, plot_price_with_ema

FAST_EMA=9
SLOW_EMA=21

# python main.py --pair EUR/USD --timeframe 1min 

def quantCoPilot(pair="EUR/USD", interval="1min"):
    
    # === 1. Fetch Data ===

    symbol = pair.replace("/", "")
    DATA_PATH = f"data/{symbol}_{interval}.csv"
    df = pd.read_csv(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    # === 2. Compute EMA Crossover ===

    df = ema_crossover(df, FAST_EMA, SLOW_EMA)
    plot_price_with_ema(df)


    # === 3. Run XGBoost ===


    # === 4. Run Regression ===


    # === 5. Run KNN ===


    # === 6. Run Random Forest ===


    # === 5. Run SVM ===




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run QuantCoPilot')
    parser.add_argument('--pair', type=str, default='BTC/USD', help='e.g. BTC/USD, ETH/USD')
    parser.add_argument('--timeframe', type=str, default='1min', help='e.g. 1min, 5min, 1h, 1day')
    args = parser.parse_args()

    quantCoPilot(pair=args.pair, interval=args.timeframe)