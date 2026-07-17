 # Real-Time Stock Portfolio Tracker

A professional, command-line financial tool built with Python. This project was developed as part of the **InternGrow Python Programming Track **.

This application allows users to build a custom investment portfolio and dynamically calculates active valuations, asset allocations, and live market pricing. It replaces static, hardcoded data with real-time stock market data fetched directly from Yahoo Finance, culminating in a structured daily Excel report.

## 🚀 Key Features

- **Live Market Integration:** Utilizes the `yfinance` library to fetch up-to-the-minute closing prices for user-defined stock tickers (e.g., AAPL, MSFT, TSLA).
- **Dynamic Valuations & Allocations:** Automatically computes the total monetary value of the portfolio and calculates the precise percentage allocation of each individual asset.
- **Automated Excel Reporting:** Uses the `pandas` library to structure the portfolio data and export a timestamped `.xlsx` summary sheet for daily financial tracking.
- **Robust Error Handling:** 
  - Automatically detects, flags, and cleans up invalid or delisted stock tickers during the API fetch phase.
  - Implements `PermissionError` handling to prevent crashes if the destination Excel file is currently open.
- **Clean CLI Interface:** Features an auto-clearing, tabular command-line interface that neatly aligns financial data, shares, and percentages for a premium user experience.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** 
  - `yfinance` (Live market data extraction)
  - `pandas` (Data structuring and manipulation)
  - `openpyxl` (Under-the-hood engine for Excel file generation)
  - `datetime`, `os` (Built-in Python modules)

## 📦 Installation & Setup

1. **Clone the Repository:**
   Clone this project to your local machine using the official InternGrow naming convention:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/InternGrow_PortfolioTracker.git](https://github.com/YOUR_GITHUB_USERNAME/InternGrow_PortfolioTracker.git)
   cd InternGrow_PortfolioTracker
