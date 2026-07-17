import yfinance as yf
import pandas as pd
from datetime import datetime
import os
from typing import Dict, List, Any

def clear_screen() -> None:

    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_portfolio() -> Dict[str, float]:
    """Prompts the user to enter their assets and quantities."""
    portfolio: Dict[str, float] = {}
    
    print("--- Portfolio Setup ---")
    print("Enter your stock ticker symbols and quantities (e.g., AAPL).")
    print("Type 'DONE' when you are finished.\n")
    
    while True:
        ticker = input("Enter stock ticker: ").upper().strip()
        
        if ticker == 'DONE':
            break
        if not ticker:
            continue
            
        try:
            quantity = float(input(f"Enter quantity for {ticker}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.\n")
                continue
            portfolio[ticker] = portfolio.get(ticker, 0) + quantity
            print(f"Added {quantity} shares of {ticker}.\n")
        except ValueError:
            print("Invalid quantity. Please enter a numerical value.\n")
            
    return portfolio

def fetch_live_prices(portfolio: Dict[str, float]) -> Dict[str, float]:
    """
    Fetches live market pricing using the yfinance library.
    Removes invalid tickers from the portfolio.
    """
    print("\nFetching live market pricing... Please wait.")
    prices: Dict[str, float] = {}
    invalid_tickers: List[str] = []
    
    for ticker in portfolio.keys():
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            
            if not hist.empty:
                prices[ticker] = float(hist['Close'].iloc[-1])
            else:
                print(f" Warning: Could not fetch price for '{ticker}'. It will be removed from the summary.")
                invalid_tickers.append(ticker)
        except Exception:
            print(f"Error fetching data for '{ticker}'. It will be removed from the summary.")
            invalid_tickers.append(ticker)
            
    # Clean up portfolio by removing invalid tickers
    for invalid in invalid_tickers:
        del portfolio[invalid]
        
    return prices

def track_portfolio() -> None:
    clear_screen()
    print("=========================================")
    print("   Real-Time Stock Portfolio Tracker   ")
    print("=========================================\n")
    
    portfolio = get_user_portfolio()
    
    if not portfolio:
        print("\nPortfolio is empty. Exiting application.")
        return

    prices = fetch_live_prices(portfolio)
    
    # Check if portfolio is empty after removing invalid tickers
    if not portfolio:
        print("\nNo valid stocks remaining to track. Exiting application.")
        return
    
    portfolio_data: List[Dict[str, Any]] = []
    total_value = 0.0
    
    for ticker, quantity in portfolio.items():
        price = prices.get(ticker, 0.0)
        value = quantity * price
        total_value += value
        
        portfolio_data.append({
            'Ticker': ticker,
            'Quantity': quantity,
            'Live Price (USD)': price,
            'Total Value (USD)': value
        })
        
    clear_screen()
    print("=================================================================")
    print("                      PORTFOLIO SUMMARY                          ")
    print("=================================================================")
    # Table Header
    print(f"{'TICKER':<10} | {'SHARES':<10} | {'PRICE (USD)':<15} | {'TOTAL VALUE':<15} | {'ALLOCATION'}")
    print("-" * 65)
    
    for item in portfolio_data:
        allocation = (item['Total Value (USD)'] / total_value) * 100 if total_value > 0 else 0.0
        item['Allocation (%)'] = allocation # Save to dict for Excel export
        
        # Print formatted table row
        print(f"{item['Ticker']:<10} | {item['Quantity']:<10} | ${item['Live Price (USD)']:<14.2f} | ${item['Total Value (USD)']:<14.2f} | {allocation:.2f}%")
        
    print("=================================================================")
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}")
    print("=================================================================")
    
    # Export to Excel
    df = pd.DataFrame(portfolio_data)
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Portfolio_Summary_{date_str}.xlsx"
    
    try:
        df.to_excel(filename, index=False)
        print(f"\n Success: Daily summary exported to '{filename}'")
    except PermissionError:
        print(f"\n Error: Cannot save '{filename}'. Please close the Excel file if it is currently open and try again.")
    except Exception as e:
        print(f"\n  Failed to export to Excel. Error: {e}")

if __name__ == "__main__":
    track_portfolio()