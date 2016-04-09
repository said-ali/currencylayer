import unittest
from client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client('0e5b880ea6ff3777c04ae0f07ca7187d')

    def test_get_live_rates(self):
        rates = self.client.live_rates()

        self.assertEqual('USD', rates['source'])
        self.assertIn('USDAED', rates['quotes'])
        self.assertIn('USDEUR', rates['quotes'])
        self.assertIn('timestamp', rates)

    def test_get_live_rates_for_GB(self):
        rates = self.client.live_rates(base_currency='GBP')

        if 'error' in rates:
            raise unittest.SkipTest(
                'SKIPPED TESTED DUE NOT HAVING ENTERPRISE ACCOUNT FOR TEST: test_get_live_rates_for_GB')
        self.assertEqual('GBP', rates['source'])
        self.assertIn('GBPAED', rates['quotes'])
        self.assertIn('GBPEUR', rates['quotes'])
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

    def test_get_live_rates_for(self):
        rates_for = self.client.live_rates_for(['EUR', 'GBP', 'AED'])

        self.assertIn('quotes', rates_for)
        self.assertIn('USDEUR', rates_for['quotes'])
        self.assertIn('USDGBP', rates_for['quotes'])
        self.assertIn('USDAED', rates_for['quotes'])
        self.assertEqual('USD', rates_for['source'])

    def test_get_historical(self):
        historical = self.client.historical('2005-02-01')

        self.assertEqual(True, historical['historical'])
        self.assertEqual('2005-02-01', historical['date'])
        self.assertEqual('USD', historical['source'])
        self.assertEqual(0.531483, historical['quotes']['USDGBP'])
        self.assertEqual(0.76715, historical['quotes']['USDEUR'])

    def test_get_historical_for_GB(self):
        historical = self.client.historical('2005-02-01', base_currency='GBP')

        if 'error' in historical:
            raise unittest.SkipTest(
                'SKIPPED TESTED DUE NOT HAVING ENTERPRISE ACCOUNT FOR TEST: test_get_historical_for_GB')

        self.assertEqual(True, historical['historical'])
        self.assertEqual('2005-02-01', historical['date'])
        self.assertEqual('GBP', historical['source'])

    def test_convert(self):
        convert_rate = self.client.convert('USD', 'GBP', 10)

        if 'error' in convert_rate:
            raise unittest.SkipTest(
                'SKIPPED TESTED DUE NOT HAVING ENTERPRISE ACCOUNT FOR TEST: test_convert')

        self.assertEqual('USD', convert_rate['query']['from'])
        self.assertEqual('GBP', convert_rate['query']['to'])
        self.assertEqual(10, convert_rate['query']['amount'])
        self.assertIsNotNone(convert_rate['query']['result'])

    def test_timeframe(self):
        time_frame = self.client.timeframe('2010-03-01', '2010-04-01', ['USD', 'GBP', 'EUR'])

        if 'error' in time_frame:
            raise unittest.SkipTest(
                'SKIPPED TESTED DUE NOT HAVING ENTERPRISE ACCOUNT FOR TEST: test_timeframe')

        self.assertEqual('2010-03-01', time_frame['start_date'])
        self.assertEqual('2010-04-01', time_frame['end_date'])

        self.assertEqual(1, time_frame['query']['quotes']['2010-03-01']['USDUSD'])
        self.assertEqual(0.668525, time_frame['query']['quotes']['2010-03-01']['USDGBP'])
        self.assertEqual(0.738541, time_frame['query']['quotes']['2010-03-01']['USDEUR'])

        self.assertEqual(1, time_frame['query']['quotes']['2010-03-02']['USDUSD'])
        self.assertEqual(0.668827, time_frame['query']['quotes']['2010-03-02']['USDGBP'])
        self.assertEqual(0.736145, time_frame['query']['quotes']['2010-03-02']['USDEUR'])


if __name__ == '__main__':
    unittest.main()
