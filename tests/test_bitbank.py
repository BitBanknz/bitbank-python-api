from bitbank import bitbank

def test_fetch_pair():
    bitbank_api = bitbank.BitBank('TEST_API_KEY')
    pair = 'USDT_BTC'
    featureset = bitbank_api.fetch_pair(pair)
    assert featureset['currency_pair'] == pair

def test_fetch_all_pairs():
    bitbank_api = bitbank.BitBank('TEST_API_KEY')
    data = bitbank_api.fetch_all_pairs()
    assert data['USDT_BTC']['currency_pair'] == 'USDT_BTC'


def test_fetch_historical_data():
    bitbank_api = bitbank.BitBank('TEST_API_KEY')
    pair = 'USDT_BTC'
    featuresets = bitbank_api.fetch_historical_featuresets(pair)
    assert featuresets[0]['currency_pair'] == pair
