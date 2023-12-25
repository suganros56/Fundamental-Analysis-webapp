from flask import render_template, request
import requests
from app import app
from datetime import date
import nsepy as nse

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form['symbol']
    
    # Retrieve real-time stock data from NSEpy
    stock_data = get_quote(symbol)
    
    # Extract relevant data for fundamental analysis
    pe_ratio = float(stock_data['PE'])
    roe = float(stock_data['ROE'])
    # Add more ratios as needed
    
    # Implement your fundamental analysis logic here
    
    # Notify the user if the stock meets the criteria
    if pe_ratio < 15 and roe > 15:
        notification = f"Potential long-term investment: {symbol}"
        # Implement notification mechanism here
    
    return render_template('result.html', symbol=symbol, pe_ratio=pe_ratio, roe=roe)

@app.route('/funda')
def fundamental():
    sbin = nse.get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))

    return sbin

