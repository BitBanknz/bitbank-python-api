

# bitbank-python-api
Python 3 API for https://BitBank.nz

See api docs at https://BitBank.nz/api

### Example usage

```
pip install bitbank

from bitbank import bitbank
```

```
bitbank_api = bitbank.BitBank('TEST_API_KEY')
pair = 'USDT_BTC'


# fetch latest forecasts for a single pair
featureset = bitbank_api.fetch_pair(pair)


# fetch latest forecasts for all pairs
pair_to_featuresets = bitbank_api.fetch_all_pairs()


# fetch historical forecasts ~4 hours of forecasts 
featuresets = bitbank_api.fetch_historical_featuresets(pair)
```

#### testing
tests ran with py.test
