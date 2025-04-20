from ta.trend import EMAIndicator



def ema_crossover(df, FAST_EMA=9, SLOW_EMA=21):

    df['ema_fast'] = EMAIndicator(df['close'], window=FAST_EMA).ema_indicator()
    df['ema_slow'] = EMAIndicator(df['close'], window=SLOW_EMA).ema_indicator()
    df['ema_cross'] = (df['ema_fast'] > df['ema_slow']).astype(int)
    df['ema_signal'] = df['ema_cross'].diff().fillna(0)

    return df

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_price_with_ema(df):
    plt.figure(figsize=(14, 6))

    # Price and EMAs
    plt.plot(df['timestamp'], df['close'], label='Price', color='black', linewidth=1)
    plt.plot(df['timestamp'], df['ema_fast'], label='EMA Fast', color='red', linestyle='--')
    plt.plot(df['timestamp'], df['ema_slow'], label='EMA Slow', color='blue', linestyle='--')

    # Crossover markers
    bullish_cross = df[df['ema_signal'] == 1]
    bearish_cross = df[df['ema_signal'] == -1]

    plt.scatter(bullish_cross['timestamp'], bullish_cross['close'],
                marker='^', color='green', label='Bullish Cross', zorder=5)

    plt.scatter(bearish_cross['timestamp'], bearish_cross['close'],
                marker='v', color='red', label='Bearish Cross', zorder=5)

    # Styling
    plt.title("Price with EMA Crossovers")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
