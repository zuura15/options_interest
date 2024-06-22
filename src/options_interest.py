from ib_api import IBAPI
from logger import logger

class OptionsInterest:
    def __init__(self):
        self.api = IBAPI()

    def fetch_metrics(self, symbol):
        if not symbol:
            logger.error("Invalid symbol provided")
            return None
        options_data = self.api.get_options_interest(symbol)
        if not options_data:
            logger.error("No options data found")
            return None
        metrics = self.extract_metrics(options_data)
        return metrics

    @staticmethod
    def extract_metrics(data):
        metrics_list = []
        for item in data:
            metrics = {
                "symbol": item.contract.symbol,
                "last_trade_date": item.contract.lastTradeDateOrContractMonth,
                "strike": item.contract.strike,
                "right": item.contract.right,
                "exchange": item.contract.exchange,
                "currency": item.contract.currency,
                "local_symbol": item.contract.localSymbol,
                "trading_class": item.contract.tradingClass
            }
            metrics_list.append(metrics)
        return metrics_list
