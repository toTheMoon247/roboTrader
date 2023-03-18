import requests

class MockAPI:
    def __init__(self, api_endpoint, api_key, api_secret):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.api_secret = api_secret
        self.token = None
        self.authenticate()

    def authenticate(self):
        self.token = 'mock_token'

    def get_apple_stock_price(self):
        headers = {'Authorization': 'Bearer ' + self.token} if self.token else {}
        response = requests.get(self.api_endpoint + 'apple/stock/price', headers=headers)
        if response.status_code == 200:
            stock_price = response.json()['price']
            return stock_price
        else:
            raise Exception('Failed to retrieve Apple stock price')

    def place_order(self, order_side, symbol, quantity, price):
        headers = {'Authorization': 'Bearer ' + self.token}
        payload = {'symbol': symbol, 'quantity': quantity, 'order_type': 'market', 'side': order_side}
        # return a fake response instead of making an HTTP request
        return {'status': 'success', 'order_id': 'fake_order_id'}

