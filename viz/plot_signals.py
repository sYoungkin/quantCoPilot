# viz/plot_signals.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_price_with_signals(df, price_col='close', signal_col='xgb_signal'):
    plt.figure(figsize=(14, 6))

    # Plot price
    plt.plot(df['timestamp'], df[price_col], label='Price', color='black', linewidth=1)

    # Optional overlays
    if 'ema_fast' in df.columns:
        plt.plot(df['timestamp'], df['ema_fast'], label='EMA Fast', linestyle='--', color='red')
    if 'ema_slow' in df.columns:
        plt.plot(df['timestamp'], df['ema_slow'], label='EMA Slow', linestyle='--', color='blue')

    # Signal markers
    if signal_col in df.columns:
        buy = df[df[signal_col] == 1]
        sell = df[df[signal_col] == 0]
        plt.scatter(buy['timestamp'], buy[price_col], marker='^', color='green', label='Buy Signal', zorder=5)
        plt.scatter(sell['timestamp'], sell[price_col], marker='v', color='orange', label='Sell Signal', zorder=5)

    # Styling
    plt.title(f"{signal_col.upper()} Signal Overlay")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.grid(True)
    plt.tight_layout()
    plt.show()