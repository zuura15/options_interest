from ib_insync import IB, Contract
from logger import logger

class IBAPI:
    def __init__(self, host='127.0.0.1', port=7496, client_id=1):
        self.host = host
        self.port = port
        self.client_id = client_id
        self.ib = IB()
        self.connect()

    def connect(self):
        try:
            self.ib.connect(self.host, self.port, self.client_id)
            logger.info("Connected to Interactive Brokers")
        except Exception as e:
            logger.error(f"Failed to connect to Interactive Brokers: {e}")

    def disconnect(self):
        self.ib.disconnect()
        logger.info("Disconnected from Interactive Brokers")

    def is_connected(self):
        return self.ib.isConnected()

    def get_options_interest(self, symbol):
        try:
            contract = Contract(symbol=symbol, secType='OPT', exchange='SMART')
            self.ib.qualifyContracts(contract)
            options_data = self.ib.reqContractDetails(contract)
            logger.info(f"Retrieved options interest for {symbol}")
            return options_data
        except Exception as e:
            logger.error(f"Error retrieving options interest for {symbol}: {e}")
            return None
