import requests


class Client(object):
    """ Client implementation for currencylayer
    """
    base_url = 'http://apilayer.net/api/'
    endpoint_live = base_url + 'live'
    endpoint_historical = base_url + 'historical'
    endpoint_convert = base_url + 'convert'
    endpoint_time_frame = base_url + 'timeframe'
    endpoint_change = base_url + 'change'
    endpoint_currencies = base_url + 'list'

    def __init__(self, access_key):
        self.client = requests.Session()
        self.client.params.update({'access_key': access_key})

    def currencies(self):
        response = self.client.get(self.endpoint_currencies)
        return response.json()

    def live_rates(self, base_currency='USD'):
        response = self.client.get(self.endpoint_live, params={'source': base_currency})
        return response.json()
