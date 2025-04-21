import pandas as pd
import argparse
from indicators.ema_crossover import ema_crossover, plot_price_with_ema
from data.fetch_data import fetch_data
from data.data_onboarding import onboard_data


FAST_EMA=9
SLOW_EMA=21



def quantCoPilot(pair="EUR/USD", interval="1min"):
    
    # === 1. Onboard Data ===

    df = onboard_data(pair, interval)


    # === 2. Compute EMA Crossover ===

    ema_crossover(df, FAST_EMA, SLOW_EMA)
    plot_price_with_ema(df)

    # === 3. Run coPilot Engine ===
    # run_models


    # === 4. Analyze Results  ===


    # === 5. Notify ===




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run QuantCoPilot')
    parser.add_argument('--pair', type=str, default='EUR/USD ', help='e.g. BTC/USD, ETH/USD')
    parser.add_argument('--timeframe', type=str, default='1min', help='e.g. 1min, 5min, 1h, 1day')
    args = parser.parse_args()

    #fetch_data(pair=args.pair, interval=args.timeframe, limit=1000)

    quantCoPilot(pair=args.pair, interval=args.timeframe)