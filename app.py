import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# Set the title of the app
st.title("Top 10 Moving Stocks Charts")

# Function to fetch stock data
def get_stock_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        data[ticker] = hist
    return data

# List of top 10 moving stocks (replace with actual tickers)
top_moving_stocks = ["AAPL", "TSLA", "AMZN", "GOOGL", "MSFT", "NVDA", "FB", "BRK-B", "JNJ", "JPM"]

# Fetch stock data
stock_data = get_stock_data(top_moving_stocks)

# Display the stock charts
for ticker, data in stock_data.items():
    st.subheader(f"{ticker} Stock Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=ticker))
    fig.update_layout(title=f"{ticker} Stock Price",
                      xaxis_title="Date",
                      yaxis_title="Close Price (USD)")
    st.plotly_chart(fig)
