import unittest
from src.options_interest import OptionsInterest

class TestOptionsInterest(unittest.TestCase):
    def setUp(self):
        self.options_interest = OptionsInterest()

    def test_fetch_metrics(self):
        symbol = "AAPL"
        metrics = self.options_interest.fetch_metrics(symbol)
        self.assertIsNotNone(metrics)
        self.assertEqual(metrics['symbol'], 'AAPL')

if __name__ == '__main__':
    unittest.main()
