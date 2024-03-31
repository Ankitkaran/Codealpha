import yfinance as yf
import pandas as pd

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            print(f"Stock '{symbol}' already exists in the portfolio.")
            return
        self.stocks[symbol] = {'quantity': quantity}

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
        else:
            print(f"Stock '{symbol}' not found in the portfolio.")

    def track_performance(self):
        total_investment = 0
        total_value = 0

        for symbol, data in self.stocks.items():
            stock = yf.Ticker(symbol)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            investment = data['quantity'] * current_price
            total_investment += investment
            total_value += investment
            print(f"Symbol: {symbol}, Quantity: {data['quantity']}, Current Price: {current_price}, Investment: {investment}")

        print(f"Total Investment: {total_investment}")
        print(f"Total Value: {total_value}")

if __name__ == "__main__":
    portfolio = Portfolio()

    # Example usage
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)

    portfolio.track_performance()

    portfolio.remove_stock("GOOGL")

    portfolio.track_performance()
