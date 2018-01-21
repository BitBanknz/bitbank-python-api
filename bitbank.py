import requests


class BitBank(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_pair(self, currency_pair):
        """

        :param currency_pair: str market pair name e.g. "BTC_ETH"
        :return: latest forecasts/featureset for the given currency_pair
        """
        try:
            request = requests.get('https://bitbank.nz/api/forecasts/' + currency_pair + '?secret=' + self.api_key)

            if request.status_code != 200:
                print("request error code: {}, {}".format(request.status_code, request.text))
            featureset = request.json()['results']
            return featureset
        except Exception as e:
            print(e)
            return None

    def fetch_all_pairs(self):
        """
        :return: pair_to_featuresets a map of currency pairs to the most up to date featureset for that pair
        """
        try:
            request = requests.get('https://bitbank.nz/api/forecasts?secret=' + self.api_key)

            if request.status_code != 200:
                print("request error code: {}, {}".format(request.status_code, request.text))
            featuresets = request.json()['results']
            pair_to_featuresets = {}
            for featureset in featuresets:
                pair_to_featuresets[featureset['currency_pair']] = featureset
            return pair_to_featuresets
        except Exception as e:
            print(e)
            return None


    def fetch_historical_featuresets(self, currency_pair):
        try:
            request = requests.get('https://bitbank.nz/api/coin/' + currency_pair + '?secret=' + self.api_key)

            if request.status_code != 200:
                print("request error code: {}, {}".format(request.status_code, request.text))
            featuresets = request.json()['results']
            return featuresets
        except Exception as e:
            print(e)
            return None
