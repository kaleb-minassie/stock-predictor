# 📈 Stock Predictor

This project is a Python-based application that utilizes historical stock data and linear regression to forecast future stock prices. This project is designed to provide a clear visual understanding of market trends by plotting actual stock performance alongside predicted values. It serves as an educational tool for those interested in finance, data science, or machine learning, offering a hands-on introduction to working with real-world data and predictive modeling techniques.


## 💡 What It Does

This project takes in a stock symbol (like `AAPL` for Apple), fetches real historical stock prices from Yahoo Finance, and then uses a basic machine learning model to predict future prices. It also creates a clear graph showing both past and predicted prices.

---

## 🔍 How It Works

1. **Data Collection**:  
   Uses the `yfinance` library to download stock price history from Yahoo Finance based on user input.

2. **Data Processing**:  
   Converts dates into a numeric format (days since the start date) to prepare for training.

3. **Prediction**:  
   Trains a **Linear Regression** model using `scikit-learn`. This model tries to fit a straight line through the historical closing prices to estimate future values.

4. **Visualization**:  
   Uses `matplotlib` to plot actual prices and predicted prices on the same graph. The graph is automatically saved as an image file.

---

## ⚙️ Features

- Interactive input (choose your stock, date range, and how many days to predict)
- Real-time data fetching
- Machine learning using Linear Regression
- Visualization with side-by-side comparison of real and predicted prices
- Saves the output plot for later use

---

## 📦 Built With

- Python 3
- [`yfinance`](https://pypi.org/project/yfinance/)
- [`pandas`](https://pandas.pydata.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`scikit-learn`](https://scikit-learn.org/)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/stock-predictor.git
cd stock-predictor
```

## 🧪 Example

When prompted:

Enter stock symbol (e.g. AAPL): AAPL
Enter start date (YYYY-MM-DD): 2023-01-01
How many days into the future to predict? (e.g. 30): 30


The script will generate and display a graph with actual and predicted closing prices, then save it as `AAPL_prediction_plot.png` in your project folder.

---

## ⚠️ Limitations

- Linear Regression is a simple model and may not perform well for highly volatile stocks.
- This predictor does **not** account for market news, events, or external factors.
- It’s meant for educational purposes — not financial advice.

---

## 🔧 Future Improvements

- Add more advanced models (e.g., LSTM, ARIMA)
- Include volume, volatility, or other financial indicators
- Add GUI or web interface using Flask or Streamlit
- Export predictions to CSV

---

## 🧠 Learning Outcomes

- Gained experience working with real-world financial data
- Practiced building a full data pipeline (input → prediction → output)
- Learned how to use Python libraries for machine learning and visualization

