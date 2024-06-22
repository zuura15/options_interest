import argparse
from options_interest import OptionsInterest
from logger import logger

def main():
    parser = argparse.ArgumentParser(description='Fetch Options Interest for a given stock symbol.')
    parser.add_argument('--symbol', type=str, help='Stock symbol to fetch the options interest for')
    args = parser.parse_args()

    symbol = args.symbol
    if not symbol:
        symbol = input("Enter the stock symbol: ")

    oi = OptionsInterest()
    metrics = oi.fetch_metrics(symbol)
    if metrics:
        logger.info(f"Options interest metrics for {symbol}: {metrics}")
        print(metrics)
    else:
        logger.error("Failed to retrieve metrics")

if __name__ == "__main__":
    main()
