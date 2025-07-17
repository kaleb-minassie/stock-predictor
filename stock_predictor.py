import yfinance as yf  # get stock data
import pandas as pd  # handle data
import matplotlib.pyplot as plt  # make plots
from sklearn.linear_model import LinearRegression  # simple ML model
import datetime  # for dates
import sys  # lets us exit on error

# ask for stock symbol
ticker = input("Enter stock symbol (e.g. AAPL): ").upper()

# ask for start date
start_date = input("Enter start date (YYYY-MM-DD): ")

# ask how many days to predict
try:
    future_days = int(input("How many days into the future to predict? (e.g. 30): "))
except ValueError:
    print("Invalid number. Try again.")
    sys.exit()

# get today’s date
end_date = datetime.date.today().strftime("%Y-%m-%d")

# try to get the data
try:
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        print("No data found for that stock and date range.")
        sys.exit()
except Exception as e:
    print("Something went wrong:", e)
    sys.exit()

# reset index so date is a column
data = data.reset_index()

# make sure 'Date' is datetime
data['Date'] = pd.to_datetime(data['Date'])

# add column for days since start
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# X = days, y = close prices
X = data[['Days']]
y = data['Close']

# train the model
model = LinearRegression()
model.fit(X, y)

# make future days for prediction
future = pd.DataFrame({'Days': range(X['Days'].max() + 1, X['Days'].max() + 1 + future_days)})
future['Predicted_Close'] = model.predict(future)

# plot actual stock prices
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], y, label="Actual Close")

# build future date range
future_dates = pd.date_range(data['Date'].max() + pd.Timedelta(days=1), periods=future_days)

# plot predicted prices
plt.plot(future_dates, future['Predicted_Close'], label="Predicted Close", linestyle='--')

# add labels and title
plt.title(f"{ticker} Stock Price Prediction")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# save and show plot
plot_filename = f"{ticker}_prediction_plot.png"
plt.savefig(plot_filename)
print(f"Prediction plot saved as: {plot_filename}")
plt.show()
