from api import MockAPI
from trader import Trader

if __name__ == '__main__':
    api_endpoint = "http://your-mock-api-endpoint.com/api/"
    api_key = "your-api-key"
    api_secret = "your-api-secret"
    mock_api = MockAPI(api_endpoint, api_key, api_secret)
    trader = Trader(mock_api)
    trader.run()
