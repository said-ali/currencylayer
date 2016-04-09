import unittest
from client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client('0e5b880ea6ff3777c04ae0f07ca7187d')

    def test_get_live_rates(self):
        rates = self.client.live_rates()

        self.assertEqual('USD', rates['source'])
        self.assertIn('USDEUR', rates['quotes'])
        self.assertIn('USDEUR', rates['quotes'])
        self.assertIn('timestamp', rates)

    def test_currencies(self):
        currencies = self.client.currencies()

        self.assertIn('currencies', currencies)
        self.assertIn('AED', currencies['currencies'])
        self.assertIn('GBP', currencies['currencies'])
        self.assertIn('EUR', currencies['currencies'])
        self.assertEqual('United Arab Emirates Dirham', currencies['currencies']['AED'])
        self.assertEqual('Euro', currencies['currencies']['EUR'])
        self.assertEqual('British Pound Sterling', currencies['currencies']['GBP'])


if __name__ == '__main__':
    unittest.main()
