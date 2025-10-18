# 📈 Volatility Forecasting in South Africa

This project explores **stock market volatility forecasting** using data from the South African financial market.  
It leverages Python, machine learning, and time series models to analyze trends, forecast volatility, and gain insights into financial risks.

---

## 🚀 Project Overview
Stock markets are dynamic, with prices moving constantly due to supply and demand, investor behavior, and economic factors.  
This project focuses on:
- Collecting financial time series data (**open, high, low, close, volume**).
- Storing and managing data in **SQLite**.
- Implementing forecasting models (e.g., **ARIMA, GARCH, ML-based approaches**).
- Analyzing volatility patterns in the South African stock market.

---

## 🛠️ Tech Stack
- **Python 3.13+**
- **SQLite** (for database management)
- **Pandas, NumPy** (data manipulation)
- **Matplotlib, Seaborn** (visualization)
- **Scikit-learn, Statsmodels** (modeling & forecasting)
- **pydantic-settings** (configuration management)

---

## 📂 Project Structure
```

Volatility-Forecasting-in-South-Africa/
│── config.py           # Configuration (API keys, DB paths, etc.)
│── database.py         # SQLite connection & queries
│── data_fetch.py       # Fetch stock data from AlphaVantage
│── analysis.ipynb      # Exploratory Data Analysis & visualizations
│── models.py           # Forecasting models (ARIMA, GARCH, ML)
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── .env                # API keys & sensitive credentials
│── stocks.sqlite       # SQLite database (generated after fetch)

````

---

## 🔑 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Volatility-Forecasting-in-South-Africa.git
cd Volatility-Forecasting-in-South-Africa
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

All dependencies are listed here. You can copy them into `requirements.txt` or install directly:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels pydantic-settings alpha_vantage
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
ALPHA_API_KEY=your_api_key_here
DB_NAME=stocks.sqlite
MODEL_DIRECTORY=models
```

### 5. Run the project

```bash
python data_fetch.py
```

---

## 📊 Example Usage

```python
from database import Database

db = Database("stocks.sqlite")
data = db.get_stock_data("JSE")  # Example for Johannesburg Stock Exchange
print(data.head())
```

---

## ✅ Features

* Fetch stock data using **AlphaVantage API**
* Store and query data in **SQLite**
* Time series forecasting using **ARIMA & GARCH**
* Visualize market trends & volatility
* Extendable to other African stock markets

---

## 🌍 Future Work

* Incorporate real-time streaming data
* Test deep learning models (**LSTM, Transformer**)
* Compare South African market with global indices
* Deploy interactive dashboards (**Plotly/Dash/Streamlit**)

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

