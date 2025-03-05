import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    
    # Get the current stock price
    stock_info = stock.history(period="1d")
    
    if stock_info.empty:
        return f"Could not find data for {ticker}"
    
    price = stock_info['Close'].iloc[0]
    currency = stock.info.get('currency', 'USD')  # Default to USD if no currency info is found
    
    # Format the price to two decimals
    formatted_price = f"{price:.2f}"
    
    return f"{ticker} price: {formatted_price} {currency}"

# Run this only if executed as a script
if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol: ").strip().upper()
    print(get_stock_price(ticker))
