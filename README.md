# crypto-tracker-99

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

crypto-tracker-99 is a Python command-line tool for tracking cryptocurrency prices and monitoring portfolio performance. It pulls real-time data from public APIs to deliver accurate market information directly in the terminal.

## Features

- Live price updates for hundreds of cryptocurrencies using the CoinGecko public API
- Portfolio tracking with automatic USD valuation and percentage change calculations
- Custom price alerts that notify users when coins cross specified thresholds
- Data export functionality to save historical prices as CSV files

## Installation

```bash
git clone https://github.com/Developer/crypto-tracker-99.git
cd crypto-tracker-99
pip install -r requirements.txt
```

## Usage

```bash
python tracker.py --coins bitcoin ethereum solana

python tracker.py --portfolio portfolio.json --export prices.csv
```