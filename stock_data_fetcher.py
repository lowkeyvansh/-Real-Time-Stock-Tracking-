import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return {
        'ticker': ticker,
        'price': data['Close'].iloc[-1],
        'volume': data['Volume'].iloc[-1],
        'time': data.index[-1].isoformat()
    }

if __name__ == "__main__":
    print(get_stock_data('AAPL'))
