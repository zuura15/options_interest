import unittest
from src.diagnostics import run_diagnostics

class TestDiagnostics(unittest.TestCase):
    def test_run_diagnostics(self):
        self.assertTrue(run_diagnostics())

if __name__ == '__main__':
    unittest.main()
