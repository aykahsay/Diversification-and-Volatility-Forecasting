# Volatility-Forecasting-in-Kenya
Got it 👍 You want **everything** (intro, setup, usage, future work, etc.) under **one single Markdown file**.
Here’s the full **README.md** you can directly use:

```markdown
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

```bash
pip install -r requirements.txt
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

## 👨‍💻 Author

**Ambachow Kahsay**
📧 [your.email@example.com](mailto:your.email@example.com)
🔗 [LinkedIn](https://linkedin.com) | [Portfolio](https://your-portfolio.com)

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```

---

👉 Do you also want me to **embed the dependencies (requirements.txt content)** directly inside this README so you don’t need a separate file?
```


outout

## 📈 Mean–Variance Analysis: Balancing Risk and Return

This section evaluates each asset’s **expected return** and **variance**, key metrics in **Modern Portfolio Theory (MPT)**.  
The goal is to understand the **risk–return trade-off** and identify assets that offer the best balance between growth potential and volatility.

---

### 🧮 1. Expected Returns (Mean of Daily Returns)

Expected return represents the **average daily performance** of each asset, derived from historical price data.

| Company Name        | Ticker | Sector       | Expected Daily Return |
|---------------------|--------|--------------|-----------------------|
| Bank of America     | BOA    | Financials   | **-2.53%**            |
| Amazon              | AMZN   | Technology   | **+68.75%**           |
| Shell               | SHEL   | Energy       | **+0.79%**            |
| Johnson & Johnson   | JNJ    | Healthcare   | **-1.87%**            |
| S&P 500 Index (SPJ) | SPJ    | Market Index | **+0.47%**            |

> ⚠️ These are **daily mean returns**. To estimate annual performance, multiply by the number of trading days (≈252).

---

### 📊 2. Variance of Daily Returns – Measuring Risk

Variance quantifies how much asset returns deviate from their mean — higher values indicate greater risk or volatility.

| Company Name        | Variance of Daily Returns | Interpretation |
|---------------------|---------------------------|----------------|
| Bank of America     | ~3.92                     | Moderate risk  |
| Amazon              | **~1390.05**              | **Extremely volatile — high risk** |
| Shell               | ~4.13                     | Moderate risk  |
| Johnson & Johnson   | ~1.35                     | Low risk       |
| S&P 500 Index (SPJ) | ~4.13                     | Market benchmark for moderate volatility |

---

### 💬 3. Interpretation

#### 🏆 **Top Performer (Return)**
* **Amazon (AMZN)** shows the **highest expected return (+68.75%)**, but its **variance is extremely high**, making it a **high-risk, high-reward** asset.

#### ⚖️ **Stable, Low-Risk Assets**
* **Shell (Energy)** and **Johnson & Johnson (Healthcare)** show **low to moderate variance**, indicating stability.
  * Shell’s **positive return** and **manageable volatility** make it a **defensive yet profitable** asset.
  * JNJ, while low risk, shows a **negative return**, making it less attractive as a standalone investment.

#### 🔻 **Underperforming Assets**
* **Bank of America (BOA)** and **Johnson & Johnson (JNJ)** show **negative mean returns**, suggesting limited upside potential unless included for **diversification benefits**.

#### 📈 **Market Benchmark**
* **S&P 500 Index (SPJ)** provides a **modest positive return (+0.47%)** with **moderate variance**, serving as a **reference point** for performance comparison.

---

### 💼 4. Portfolio Implications

The Mean–Variance analysis suggests:

- **Amazon** contributes **growth potential** but increases volatility.
- **Shell** and **Johnson & Johnson** provide **stability** and help **reduce total portfolio risk**.
- Combining **low-correlation** and **moderate-risk** assets across different sectors can create an **efficient portfolio**.


## ⚖️ Sharpe Ratio Analysis – Risk-Adjusted Performance

The **Sharpe Ratio** measures how effectively an asset compensates investors for the risk taken.  
It compares each asset’s **excess return** (above the risk-free rate) to its **volatility**.

> Formula:  
> \[
> \text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
> \]  
> where \( R_p \) = average portfolio return, \( R_f \) = risk-free rate, and \( \sigma_p \) = standard deviation of returns.

---

### 🧮 1. Computed Results

| Asset (Ticker) | Expected Daily Return | Volatility (Std Dev) | Sharpe Ratio |
|----------------|-----------------------|----------------------|---------------|
| **Bank of America (BOA)** | -0.0253% | 1.9803% | **-0.0228** |
| **Amazon (AMZN)** | +0.6876% | 37.2834% | **0.0179** |
| **Shell (SHEL)** | +0.0079% | 2.0321% | **-0.0059** |
| **Johnson & Johnson (JNJ)** | -0.0187% | 1.1649% | **-0.0331** |
| **S&P 500 Index (SPJ)** | +0.0047% | 2.0332% | **-0.0074** |

---

### 📊 2. Interpretation

| Sharpe Ratio Range | Evaluation | Meaning |
|--------------------|-------------|----------|
| **> 1.0** | Excellent | High returns relative to risk |
| **0.5 – 1.0** | Good | Acceptable risk-adjusted returns |
| **0 – 0.5** | Moderate | Marginal improvement over risk-free rate |
| **< 0** | Poor | Underperforming relative to risk-free rate |

---

### 💡 3. Insights

- **Amazon (AMZN)** shows the **highest Sharpe Ratio (0.0179)** — although still very low, it performs *slightly better* on a risk-adjusted basis than other assets.  
  *However, its high volatility (37.28%) makes it risky.*

- **Bank of America (BOA)** and **Johnson & Johnson (JNJ)** have **negative Sharpe Ratios**, indicating that their returns do **not** adequately compensate for risk — they underperform the risk-free benchmark.

- **Shell (SHEL)** and **S&P 500 (SPJ)** also show slightly **negative Sharpe Ratios**, meaning their daily returns are too small relative to volatility.

---

### 🧭 4. Takeaway

Current results suggest that:
- None of the assets are generating **strong risk-adjusted returns** at the daily level.  
- **Amazon** remains the most promising but volatile choice.  
- Combining **low-correlated** assets (from earlier covariance analysis) may **improve the overall Sharpe Ratio** through diversification.

---

### 🚀 Next Steps

To enhance portfolio performance:
- Compute a **Portfolio Sharpe Ratio** using weighted returns.  
- Explore the **Efficient Frontier** to identify the **optimal mix** of assets with the highest Sharpe Ratio.  
- Annualize returns and risk to provide a clearer long-term performance comparison.

## 🚀 Efficient Frontier & Optimal Portfolio – Maximizing Risk-Adjusted Returns

The **Efficient Frontier** represents all possible portfolios that offer the **highest expected return for a given level of risk**.  
By simulating multiple weight combinations, we identify the **Optimal Portfolio** — the one that **maximizes the Sharpe Ratio**.

---

### 🧾 1. Optimal Portfolio Summary

| Metric | Value | Interpretation |
|---------|--------|----------------|
| **Expected Daily Return** | **0.0048 (≈ 0.48%)** | The portfolio’s average expected daily return. |
| **Volatility (Std Dev)** | **0.2616 (≈ 26.16%)** | Indicates moderate risk — average fluctuation in daily returns. |
| **Sharpe Ratio** | **0.0177** | Measures risk-adjusted performance — the portfolio earns slightly above the risk-free rate. |

> ⚙️ The Sharpe Ratio is relatively low at the daily level. However, annualizing returns (×252) and volatility (×√252) typically increases this value and offers a clearer long-term perspective.

---

### 📈 2. Interpretation

- The **Optimal Portfolio** achieves the **highest Sharpe Ratio (0.0177)** among all simulated portfolios — meaning it offers the **best trade-off between risk and return**.
- With an **expected daily return of 0.48%**, it slightly outperforms individual assets in terms of efficiency.
- **Volatility (26%)** reflects a **moderate risk exposure**, acceptable for diversified portfolios aiming for steady growth.
- Combining assets from **different sectors** (Technology, Energy, Healthcare, and Financials) reduces total variance through diversification effects.

---

### 🌐 3. Efficient Frontier Visualization

The plot below illustrates the **Efficient Frontier**:

- **Scatter Points (Green–Yellow Gradient):** Thousands of random portfolios with different weight combinations.  
- **Upper Boundary:** The Efficient Frontier — where portfolios achieve **maximum return for each risk level**.  
- **Red Star (★):** The **Optimal Portfolio**, offering the **highest Sharpe Ratio**.

*(See “Efficient Frontier” plot in your analysis notebook.)*

---

### 💡 4. Key Insights

| Aspect | Observation | Implication |
|---------|--------------|-------------|
| **Return vs Risk** | Optimal portfolio yields moderate return for moderate risk | Balanced profile suitable for medium-risk investors |
| **Sharpe Ratio** | 0.0177 → low daily but positive | Indicates improvement through diversification |
| **Diversification Benefit** | Achieved via low-correlated assets (Amazon, Shell, JNJ) | Reduces volatility without large return sacrifice |

---

### ✅ 5. Strategic Takeaway

To further enhance performance:
- **Annualize the portfolio Sharpe Ratio** for realistic interpretation.  
- Compare this optimal portfolio with the **market index (S&P 500)** to gauge outperformance.  
- Conduct **backtesting** or **rolling Sharpe analysis** to validate consistency over time.  

---
## 🧩 Portfolio Weight Optimization – Asset Allocation Strategy

This section presents the **optimal asset allocation** that achieves the **highest Sharpe Ratio**, providing the best balance between expected return and risk.

---

### 🧮 1. Optimization Process

A **Monte Carlo simulation** of 10,000 random portfolios was performed using the assets:

- Bank of America (Financials)  
- Amazon (Technology)  
- Shell (Energy)  
- Johnson & Johnson (Healthcare)  
- S&P 500 Index (Market Benchmark)

Each simulation calculated:
- **Expected Return**
- **Portfolio Volatility**
- **Sharpe Ratio**

The portfolio with the **maximum Sharpe Ratio** was selected as the **optimal portfolio**.

---

### 💼 2. Optimal Weights (Example Output)

| Asset | Optimal Weight (%) | Interpretation |
|--------|--------------------|----------------|
| **Bank of America** | 10.5% | Provides financial sector exposure |
| **Amazon** | 38.2% | Growth driver, highest return potential |
| **Shell** | 22.4% | Energy diversification and moderate risk |
| **Johnson & Johnson** | 18.6% | Stability and defensive characteristics |
| **S&P 500 Index** | 10.3% | Benchmark and broad market balance |

> ⚠️ *These percentages are illustrative; actual results depend on simulation output.*

---

### 📊 3. Interpretation

- The **largest weight** is allocated to **Amazon**, due to its **high expected return**.  
- **Shell** and **Johnson & Johnson** provide **sectoral balance** and **volatility reduction**.  
- **Bank of America** and the **S&P 500 Index** serve as **market-linked stabilizers**.  
- The diversified mix reduces unsystematic risk and enhances overall **Sharpe performance**.

---

### 🧠 4. Key Takeaway

This allocation achieves the **optimal risk-adjusted performance** among all tested portfolios.  
Future work can include:
- Annualized return and volatility comparison  
- Dynamic rebalancing based on market trends  
- Incorporating **constraints** (e.g., max weight per sector)

---
## 🧮 Optimal Portfolio Performance Summary

### 📊 Key Performance Metrics

| Metric | Value | Interpretation |
|:--------|:------:|:---------------|
| **Expected Daily Return** | **0.5122%** | The portfolio is expected to earn approximately **0.51% per day** on average. |
| **Volatility (Risk)** | **0.2775%** | The portfolio’s daily value fluctuates by about **0.28%**, indicating **moderate risk**. |
| **Sharpe Ratio** | **1.8451** | **Excellent performance** — for every 1 unit of risk, the portfolio earns **1.85 units of excess return**. |

---

### 💡 Interpretation

The optimal portfolio demonstrates **strong risk-adjusted returns**, as shown by a **Sharpe Ratio > 1.8**.  
This means the portfolio efficiently balances **expected return and volatility**.

The allocation is heavily weighted toward **Amazon (74.41%)** and **Shell (17.27%)**, reflecting assets that drive higher returns while controlling for risk.  
Such a portfolio is **ideal for growth-oriented investors** seeking **maximum performance** with **manageable volatility**.

---

### 📈 Portfolio Allocation Summary

| Asset | Optimal Weight (%) |
|:------|:------------------:|
| Bank of America | 1.89 |
| Amazon | 74.41 |
| Shell | 17.27 |
| Johnson & Johnson | 2.70 |
| S&P 500 Index | 3.73 |

---

### ✅ Insights

- **High Sharpe Ratio (1.845)** → Strong risk-adjusted performance.  
- **Moderate Volatility (0.28%)** → Stable daily fluctuations.  
- **Amazon** is the **dominant contributor** to expected return.  
- The **diversified combination** still reduces unsystematic risk.