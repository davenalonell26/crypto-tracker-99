# Crypto-Tracker-99

Crypto-Tracker-99 is a lightweight Python command-line utility designed to monitor real-time cryptocurrency price fluctuations and portfolio value changes. It provides actionable insights and automated alerts, ensuring you stay informed on market volatility without constant manual checking.

### Features

*   **Live Market Data:** Fetches instantaneous pricing for top-tier assets using the CoinGecko API.
*   **Portfolio Snapshot:** Calculates total holdings performance based on custom purchase prices and current market rates.
*   **Price Threshold Alerts:** Notifies users via terminal output when a specific coin breaches a pre-defined high or low valuation.
*   **Data Exporting:** Exports historical tracking data to CSV format for external analysis in Excel or Google Sheets.

### Installation

Ensure you have Python 3.8+ installed, then follow these steps:

```bash
# Clone the repository
git clone https://github.com/Developer/crypto-tracker-99.git
cd crypto-tracker-99

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

To initialize the tracker and view current prices for your configured watchlist, run:

```bash
python main.py --watchlist BTC,ETH,SOL
```

To run an automated monitor that checks for price spikes every 60 seconds:

```bash
python main.py --monitor --interval 60 --threshold 5
```

### Configuration
Update the `config.json` file in the root directory to define your API keys and your personal portfolio quantity for accurate PnL tracking.

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.