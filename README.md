# Stock Data Analysis and GARCH Modeling

This repository provides a complete workflow for retrieving, storing, analyzing, and modeling stock price data. It integrates the AlphaVantage API with a SQLite database and includes tools for return analysis and volatility modeling using GARCH models.

---

## Overview

The project consists of two main components:

1. **Data Acquisition and Storage**
   - Fetches daily stock price data from the AlphaVantage API.
   - Stores the data in a local SQLite database for efficient access and reuse.
   - Ensures data is clean, structured, and ready for analysis.

2. **Data Analysis and Volatility Modeling**
   - Computes daily returns, expected returns, and variances for multiple stocks.
   - Fits GARCH (Generalized Autoregressive Conditional Heteroskedasticity) models to estimate and forecast stock volatility.
   - Provides tools for exploratory data analysis (EDA), including visualization of returns and volatility trends.

---

## Key Features

- Easy-to-use interface for downloading and managing stock data.
- Supports multiple tickers and historical data ranges.
- Stores data locally to avoid repeated API calls.
- Clean and formatted data for financial modeling and analysis.
- Volatility forecasting using GARCH models.
- Ready for integration into broader quantitative finance or trading strategies.

---

## Project Structure

- **AlphaVantage API Wrapper** – Handles fetching stock data and formatting it for analysis.
- **SQLite Repository** – Manages storing and retrieving stock data efficiently.
- **GARCH Modeling** – Fits volatility models and generates forecasts for risk analysis.
- **Exploratory Data Analysis (EDA)** – Tools for analyzing returns, variance, and trends.

---

## Purpose

This repository is designed to:

- Simplify access to historical stock data.
- Provide a reproducible framework for financial analysis.
- Enable volatility modeling for investment and risk management decisions.
- Serve as a foundation for further quantitative finance projects, including predictive modeling and portfolio optimization.

---

## License

MIT License.
