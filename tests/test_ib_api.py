import unittest
from src.ib_api import IBAPI

class TestIBAPI(unittest.TestCase):
    def setUp(self):
        self.api = IBAPI()

    def test_connection(self):
        self.assertTrue(self.api.is_connected())

    def test_get_options_interest(self):
        symbol = "AAPL"
        data = self.api.get_options_interest(symbol)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
