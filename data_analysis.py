import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()

def fetch_data(ticker):
    cursor.execute('SELECT time, price FROM stock_data WHERE ticker = ?', (ticker,))
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['time', 'price'])
    df['time'] = pd.to_datetime(df['time'])
    return df

def plot_stock_price(ticker):
    df = fetch_data(ticker)
    plt.plot(df['time'], df['price'], label=ticker)
    plt.title(f'{ticker} Price Over Time')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_stock_price('AAPL')
