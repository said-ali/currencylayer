currencylayer
=============
.. image:: https://img.shields.io/pypi/v/currencylayer.svg
:target: https://pypi.python.org/pypi/currencylayer
    :alt: Latest PyPI version

        Python API client for currencylayer. This library supports all API access provide by currencylayer.
        This package is compatible with Python 2.7, 3.0 to 3.5

Basic Use
---------
To use currencylayer, you must first create a `Client` instance,
passing the access key id you obtained when you registered
with currencylayer:

.. code:: python

    import currencylayer
    exchange_rate = currencylayer.Client(access_key=YOUR_ACCESS_KEY)
    exchange_rate.currencies()
    e.g reponse
        {
            "terms": "https://currencylayer.com/terms",
            "privacy": "https://currencylayer.com/privacy",
            "timestamp": 1430401802,
            "source": "USD",
            "quotes": {
            "USDAED": 3.672982,
            "USDAFN": 57.8936,
             [...]
             }
        }

Live Rates
---------
To get live rates, Call live_rates method and pass optional currency

.. code:: python

    import currencylayer
    exchange_rate = currencylayer.Client(access_key=YOUR_ACCESS_KEY)
    exchange_rate.live_rates(base_currency='GBP')
    e.g reponse
        {
            "success": true,
            "terms": "https://currencylayer.com/terms",
            "privacy": "https://currencylayer.com/privacy",
            "timestamp": 1430068515,
            "source": "GBP",
            "quotes": {
            "GBPAED": 5.578448,
            "GBPAFN": 87.869413,
            "GBPALL": 196.414724,
            "GBPAMD": 719.087298,
            "GBPANG": 2.717836,
            "GBPAOA": 165.601846,
            "GBPARS": 13.514458,
            "GBPAUD": 1.941526,
            [...]
            }
        }

Live Rates for Specific Currencies
---------
To get live rates, for specific currencies Call live_rates_for method and pass optional array of currencies e.g ['EUR', 'GBP', 'AED'] and and optional base currency

.. code:: python

    import currencylayer
    exchange_rate = currencylayer.Client(access_key=YOUR_ACCESS_KEY)
    exchange_rate.test_get_live_rates_for(currencies=['AUD','CHF','EUR','GBP','PLN'], base_currency='USD')
    e.g reponse
        {
            "success": true,
            "terms": "https://currencylayer.com/terms",
            "privacy": "https://currencylayer.com/privacy",
            "timestamp": 1430068515,
            "source": "USD",
            "quotes": {
            "USDAUD": 1.278384,
            "USDCHF": 0.953975,
            "USDEUR": 0.919677,
            "USDGBP": 0.658443,
            "USDPLN": 3.713873
            }
        }

Historical Rates
---------
To get historical rates, Call historical method and pass date and currency. If no date or currency is provided current date and USD is used. Date format required is YEAR-MONTH-DAY

.. code:: python

    import currencylayer
    exchange_rate = currencylayer.Client(access_key=YOUR_ACCESS_KEY)
    exchange_rate.historical(date='2005-02-01', base_currency='USD')
    e.g reponse
        {
          "success": true,
          "terms": "https://currencylayer.com/terms",
          "privacy": "https://currencylayer.com/privacy",
          "historical": true,
          "date": "2005-02-01",
          "timestamp": 1107302399,
          "source": "USD",
          "quotes": {
            "USDAED": 3.67266,
            "USDALL": 96.848753,
            "USDAMD": 475.798297,
            "USDANG": 1.790403,
            "USDARS": 2.918969,
            "USDAUD": 1.293878,
            [...]
          }
        }


Currency Conversion
---------
To convert rate from one currency to another, Call convert method and pass three required parameter. from_currency, to_currency, amount and optional date.

.. code:: python

    import currencylayer
    exchange_rate = currencylayer.Client(access_key=YOUR_ACCESS_KEY)
    exchange_rate.convert(from_currency='USD', to_currency='GBP', amount=10)
    e.g reponse
        {
          "success": true,
          "terms": "https://currencylayer.com/terms",
          "privacy": "https://currencylayer.com/privacy",
          "query": {
            "from": "USD",
            "to": "GBP",
            "amount": 10
          },
          "info": {
            "timestamp": 1430068515,
            "quote": 0.658443
          },
          "result": 6.58443
        }

Time-Frame Queries
---------
To request the change (both margin and percentage) of one or more currencies, relative to a Source Currency, within a specific time-frame (optional).
Call change_queries and pass three required parameters. start_date, end_date, currencies which must be a list and optional base_currency
.. code:: python

    import currencylayer
    exchange_rate = currencylayer.Client(access_key=YOUR_ACCESS_KEY)
    exchange_rate.change_queries(start_date='2010-03-01', end_date='2010-04-01', currencies=['AUD','EUR','MXN'])
    e.g reponse
            {
              "success": true,
              "terms": "https://currencylayer.com/terms",
              "privacy": "https://currencylayer.com/privacy",
              "change": true,
              "start_date": "2005-01-01",
              "end_date": "2010-01-01",
              "source": "USD",
              "quotes": {
                "USDAUD": {
                  "start_rate": 1.281236,
                  "end_rate": 1.108609,
                  "change": -0.1726,
                  "change_pct": -13.4735
                },
                "USDEUR": {
                  "start_rate": 0.73618,
                  "end_rate": 0.697253,
                  "change": -0.0389,
                  "change_pct": -5.2877
                },
                "USDMXN":{
                  "start_rate": 11.149362,
                  "end_rate": 13.108757,
                  "change": 1.9594,
                  "change_pct": 17.5741
                }
              }
            }


Unit Test
---------
To tun unit test run:

.. code:: python

    python test.py



Installation
============

Install the latest release with:

::

    pip install currencylayer


Compatibility
-------------
Python 2.7, 3.0 to 3.5


Authors
-------

`currencylayer` was written by `Said Ali <said.ali@msn.com>`_.
