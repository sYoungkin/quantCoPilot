from ta.trend import EMAIndicator
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



def ema_crossover(df, FAST_EMA=9, SLOW_EMA=21):

    df['ema_fast'] = EMAIndicator(df['close'], window=FAST_EMA).ema_indicator()
    df['ema_slow'] = EMAIndicator(df['close'], window=SLOW_EMA).ema_indicator()
    df['ema_cross'] = (df['ema_fast'] > df['ema_slow']).astype(int)
    df['ema_signal'] = df['ema_cross'].diff().fillna(0)

    return df

# def plot_price_with_ema(df):
#     fig, ax = plt.subplots(figsize=(14, 6))
#     ax.set_facecolor("#ddd")  # Optional: light grey background

#     # Price and EMAs
#     ax.plot(df['timestamp'], df['close'], label='Price', color='black', linewidth=1)
#     ax.plot(df['timestamp'], df['ema_fast'], label='EMA Fast', color='red', linestyle='--')
#     ax.plot(df['timestamp'], df['ema_slow'], label='EMA Slow', color='blue', linestyle='--')

#     # Crossover markers
#     bullish_cross = df[df['ema_signal'] == 1]
#     bearish_cross = df[df['ema_signal'] == -1]

#     ax.scatter(bullish_cross['timestamp'], bullish_cross['close'],
#                marker='^', color='green', label='Bullish Cross', zorder=5)

#     ax.scatter(bearish_cross['timestamp'], bearish_cross['close'],
#                marker='v', color='red', label='Bearish Cross', zorder=5)

#     # Fix datetime axis
#     locator = mdates.AutoDateLocator()
#     formatter = mdates.DateFormatter('%Y-%m-%d %H:%M')
#     ax.xaxis.set_major_locator(locator)
#     ax.xaxis.set_major_formatter(formatter)

#     # Styling
#     ax.set_title("Price with EMA Crossovers")
#     ax.set_xlabel("Time")
#     ax.set_ylabel("Price")
#     ax.legend()
#     ax.grid(True)

#     fig.autofmt_xdate()  # Auto-rotate dates for readability
#     fig.tight_layout()
#     plt.show()
