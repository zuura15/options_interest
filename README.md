# Options Interest App

## Overview
The Options Interest App allows you to retrieve and explore options interest metrics for any given symbol using the Interactive Brokers API.

## Important Options Interest Metrics
- **symbol**: The symbol of the option.
- **last_trade_date**: The last trade date or contract month.
- **strike**: The strike price of the option.
- **right**: The right (call or put) of the option.
- **exchange**: The exchange where the option is traded.
- **currency**: The currency in which the option is denominated.
- **local_symbol**: The local symbol of the option.
- **trading_class**: The trading class of the option.

## Setup
1. Install the required dependencies:
    ```bash
    pip install ib_insync
    pip install python-dotenv
    ```

2. Configure the Interactive Brokers API connection in `config/settings.py`.

3. Run the app:
    ```bash
    python src/main.py
    ```

## Diagnostic Mode
To run diagnostics and check the connection to Interactive Brokers:
```bash
python src/diagnostics.py
```

## Running Unit Tests
To run the unit tests:
```bash
python -m unittest discover tests
```

## Usage
The main functionality is implemented in the `OptionsInterest` class, which allows fetching options interest metrics for any given symbol.
