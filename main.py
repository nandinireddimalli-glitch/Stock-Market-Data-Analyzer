
from src.data_fetcher import fetch_stock_data, load_sample_data
from src.data_cleaner import clean_stock_data
from src.technical_indicators import calculate_technical_indicators
from src.stock_analyzer import analyze_stock_data, display_analysis
from src.risk_analyzer import analyze_stock_risk, display_risk_analysis
from src.visualization import create_visualizations
from src.report_generator import generate_report

import os
import pandas as pd


def main():

    print("\n" + "=" * 60)
    print("          STOCK MARKET DATA ANALYZER")
    print("=" * 60)

    print("\nSelect Data Source:")
    print("1. Live Stock Market Data (Yahoo Finance)")
    print("2. Offline Sample Dataset")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":

        ticker = input(
            "\nEnter stock ticker (Example: AAPL, TCS.NS): "
        ).strip().upper()

        if not ticker:
            print("Invalid ticker symbol.")
            return

        period = input(
            "Enter period (1y, 2y, 5y, max) [default: 1y]: "
        ).strip()

        if not period:
            period = "1y"

        raw_data = fetch_stock_data(ticker, period)

    elif choice == "2":

        ticker = "SAMPLE_STOCK"

        raw_data = load_sample_data()

        print("\nUsing synthetic offline sample data.")
        print("This dataset does not represent actual market prices.")

    else:
        print("\nInvalid choice. Please select 1 or 2.")
        return

    # Step 1: Clean data.
    cleaned_data = clean_stock_data(raw_data)

    # Step 2: Calculate technical indicators.
    analyzed_data = calculate_technical_indicators(
        cleaned_data
    )

    # Step 3: Analyze stock performance.
    analysis = analyze_stock_data(analyzed_data)

    # Step 4: Analyze historical risk.
    risk_analysis = analyze_stock_risk(analyzed_data)

    # Step 5: Display analysis.
    display_analysis(analysis)

    display_risk_analysis(risk_analysis)

    # Step 6: Save analyzed dataset.
    os.makedirs("outputs", exist_ok=True)

    csv_path = f"outputs/{ticker}_analyzed_data.csv"

    analyzed_data.to_csv(csv_path)

    print(f"\nAnalyzed dataset saved: {csv_path}")

    # Step 7: Generate charts.
    create_visualizations(analyzed_data, ticker)

    # Step 8: Generate report.
    report_path = generate_report(
        ticker,
        analysis,
        risk_analysis
    )

    print("\n" + "=" * 60)
    print("             PROJECT EXECUTION COMPLETED")
    print("=" * 60)

    print(f"\nDataset: {csv_path}")
    print("Charts: images/")
    print(f"Report: {report_path}")

    print("\nThank you for using Stock Market Data Analyzer!")


if __name__ == "__main__":
    main()
