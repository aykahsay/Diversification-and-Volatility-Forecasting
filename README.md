# Diversification & Volatility Forecasting

> A quantitative finance and data engineering system for modeling, forecasting, and optimizing financial market risk using data from .

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?style=flat-square&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57?style=flat-square&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## Overview

Financial markets exhibit **time-varying volatility**, making risk prediction essential for portfolio optimization, risk management, and asset allocation. This project builds a complete end-to-end pipeline:

```
API  →  Data Ingestion  →  SQLite Storage  →  GARCH Modeling  →  Portfolio Optimization  →  Insights
```

---

## Core Objectives

- Model **volatility clustering** using GARCH(1,1)
- Analyze **risk-return trade-offs** via Mean–Variance Analysis
- Optimize portfolios using the **Efficient Frontier**
- Evaluate performance using the **Sharpe Ratio**
- Build a **scalable, modular data pipeline**

---

## Tech Stack

| Layer | Tools |
|---|---|
| **Core** | Python 3.10+, SQLite, Pandas, NumPy |
| **Modelling** | `arch` (GARCH), statsmodels, scikit-learn |
| **Backend** | FastAPI, Uvicorn |
| **Config** | pydantic-settings, `.env` |

---

## Project Structure

```
diversification-volatility-forecasting/
│
├── api/                    # API integrations (AlphaVantage)
├── pipeline/               # Workflow orchestration
├── processing/             # Data cleaning & feature engineering
├── models/
│   └── volatility_model.py # GARCH implementation
├── db/                     # Database logic
├── data/
│   └── stocks.sqlite
├── notebooks/              # Analysis & experiments
├── config/
│   └── settings.py
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/diversification-volatility-forecasting.git
cd diversification-volatility-forecasting
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file in the root directory:

```env
ALPHA_API_KEY=your_api_key_here
DB_NAME=stocks.sqlite
MODEL_DIRECTORY=./models
```

### 5. Run the project

```bash
python main.py
```

### 6. Launch the API server (optional)

```bash
uvicorn main:app --reload --port 8008
```

API docs available at: `http://localhost:8008/docs`

---

## Analytical Components

### GARCH(1,1) Volatility Model

Captures time-varying risk that static models miss:

```
σ²ₜ = ω + α·ε²ₜ₋₁ + β·σ²ₜ₋₁
```

- `ω` — long-run variance
- `α` — sensitivity to recent shocks
- `β` — persistence of past volatility

### Sharpe Ratio

```
Sharpe = (Rₚ − Rƒ) / σₚ
```

Measures excess return per unit of risk. Higher values indicate better risk-adjusted performance.

### Mean–Variance Analysis

Evaluates expected return vs. risk across the asset universe:

| Asset | Profile |
|---|---|
| Amazon | High return, high risk |
| Shell | Balanced and stable |
| JNJ | Low risk, defensive |
| S&P 500 | Market benchmark |

### Efficient Frontier

Simulates thousands of portfolio combinations to identify the optimal risk-return curve and the maximum Sharpe ratio portfolio.

---

## Results

### Optimal Portfolio Weights

| Asset | Weight |
|---|---|
| Amazon | 74.41% |
| Shell | 17.27% |
| Others | 8.32% |

### Performance Summary

| Metric | Value |
|---|---|
| Expected Daily Return | 0.51% |
| Daily Volatility | 0.28% |
| Sharpe Ratio | **1.845** |

---

## Key Insights

- **Volatility is time-varying** — GARCH outperforms static models by capturing clustering effects
- **Diversification works** — combining uncorrelated assets measurably reduces portfolio risk
- **Return comes with risk** — high-return assets increase overall volatility; balance is essential
- **Efficient frontier is actionable** — identifies the exact weights that maximise risk-adjusted return

---

## Engineering Highlights

- Modular architecture separating API, pipeline, models, and database layers
- Environment-based configuration via `.env` and pydantic-settings
- SQLite-backed workflow for reproducibility and portability
- FastAPI layer for serving model outputs as a REST API

---

## Roadmap

- [ ] Real-time data streaming
- [ ] Deep learning models (LSTM, Transformers)
- [ ] Advanced risk metrics (VaR, CVaR)
- [ ] Interactive dashboard (Streamlit / Plotly)

---

## Author

**Ambachow Kahsay**
Data Science · Quantitative Finance · Software Engineering

- GitHub: [github.com/aykahsay](https://github.com/aykahsay)
- LinkedIn: [linkedin.com/in/ambachow-kahsay-863b7b291](https://linkedin.com/in/ambachow-kahsay-863b7b291)

---

## License

MIT License — see [LICENSE](LICENSE) for details.
