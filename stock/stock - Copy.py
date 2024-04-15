import yfinance as yf

class Stock:
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity
        self.data = None
    
    def fetch_data(self):
        self.data = yf.Ticker(self.symbol).history(period="1d")
    
    def current_price(self):
        if self.data is None:
            self.fetch_data()
        return self.data['Close'].iloc[-1]

class Portfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol].quantity += quantity
        else:
            stock = Stock(symbol, quantity)
            self.stocks[symbol] = stock
    
    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
        else:
            print("Stock not found in portfolio.")
    
    def update_quantity(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol].quantity = quantity
        else:
            print("Stock not found in portfolio.")
    
    def current_value(self):
        total_value = 0
        for stock in self.stocks.values():
            total_value += stock.current_price() * stock.quantity
        return total_value

    def display_portfolio(self):
        print("Stock\t\tQuantity\tCurrent Price\tTotal Value")
        print("-" * 50)
        for symbol, stock in self.stocks.items():
            current_price = stock.current_price()
            total_value = current_price * stock.quantity
            print(f"{symbol}\t\t{stock.quantity}\t\t${current_price:.2f}\t\t${total_value:.2f}")
        print("-" * 50)
        print(f"Total Portfolio Value: ${self.current_value():.2f}")

# Example usage:
portfolio = Portfolio()
portfolio.add_stock("AAPL", 10)  # Add 10 shares of Apple
portfolio.add_stock("MSFT", 5)   # Add 5 shares of Microsoft

portfolio.display_portfolio()

portfolio.update_quantity("AAPL", 15)  # Update quantity of Apple to 15 shares
portfolio.add_stock("GOOG", 3)        # Add 3 shares of Google
portfolio.remove_stock("MSFT")         # Remove Microsoft from portfolio

portfolio.display_portfolio()
