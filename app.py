from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock/<ticker>')
def stock_data(ticker):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT time, price FROM stock_data WHERE ticker = ? ORDER BY time DESC LIMIT 1', (ticker,))
    data = cursor.fetchone()
    conn.close()
    return jsonify({'ticker': ticker, 'price': data[1], 'time': data[0]})

@app.route('/historical/<ticker>')
def historical_data(ticker):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT time, price FROM stock_data WHERE ticker = ?', (ticker,))
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
