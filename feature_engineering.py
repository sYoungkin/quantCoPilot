# feature_engineering.py
import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

def generate_features(df):
    df = df.copy()
    df['return_1'] = df['close'].pct_change()
    df['return_3'] = df['close'].pct_change(3)
    df['ema_fast'] = df['close'].ewm(span=5).mean()
    df['ema_slow'] = df['close'].ewm(span=20).mean()
    df['macd'] = df['ema_fast'] - df['ema_slow']
    df['rsi'] = RSIIndicator(df['close']).rsi()
    bb = BollingerBands(df['close'])
    df['boll_upper'] = bb.bollinger_hband()
    df['boll_lower'] = bb.bollinger_lband()
    df = df.dropna()
    return df