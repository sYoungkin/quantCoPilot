import pandas as pd
import argparse
from indicators.ema_crossover import ema_crossover
from data.data_onboarding import onboard_data
from copilot.copilot_engine import run_models
#from viz.plot_signals import plot_price_with_signals


FAST_EMA=9
SLOW_EMA=21



def quantCoPilot(pair="EURUSD", interval="1min"):
    
    # === 1. Onboard Data ===

    df = onboard_data(pair, interval)


    # === 2. Compute EMA Crossover ===

    df = ema_crossover(df, FAST_EMA, SLOW_EMA)
    #plot_price_with_ema(df)

    
    # === 3. Run coPilot Engine ===
    df = run_models(df)


    # === 4. Analyze Results  ===


    # === 5. Notify ===




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run QuantCoPilot')
    parser.add_argument('--pair', type=str, default='EURUSD ', help='e.g. BTCUSD, ETHUSD')
    parser.add_argument('--timeframe', type=str, default='1m', help='e.g. 1m, 5m, 1h, 1d')
    args = parser.parse_args()

    #fetch_data(pair=args.pair, interval=args.timeframe, limit=1000)

    quantCoPilot(pair=args.pair, interval=args.timeframe)