import requests

class MockAPI:
    def __init__(self, api_endpoint, api_key, api_secret):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.api_secret = api_secret
        self.token = None

    def authenticate(self):
        payload = {'api_key': self.api_key, 'api_secret': self.api_secret}
        response = requests.post(self.api_endpoint + 'authenticate', data=payload)
        if response.status_code == 200:
            self.token = response.json()['token']
        else:
            raise Exception('Failed to authenticate with the API')

    def get_apple_stock_price(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        response = requests.get(self.api_endpoint + 'apple/stock/price', headers=headers)
        if response.status_code == 200:
            stock_price = response.json()['price']
            return stock_price
        else:
            raise Exception('Failed to retrieve Apple stock price')

    def place_order(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        payload = {'symbol': 'AAPL', 'quantity': 1, 'order_type': 'market', 'side': 'buy'}
        response = requests.post(self.api_endpoint + 'orders/place', headers=headers, data=payload)
        if response.status_code == 200:
            print('Order placed successfully')
        else:
            raise Exception('Failed to place order')
