from api import MockAPI

class Trader:
    def __init__(self, api):
        self.api = api

    def trade(self):
        self.api.authenticate()
        stock_price = self.api.get_apple_stock_price()
        if stock_price >= 100:
            self.api.place_order()
