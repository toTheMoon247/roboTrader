import random
import time

class Trader:
    def __init__(self, api):
        self.api = api
        self.symbol = 'AAPL'
        self.target_price = 100

    def trade(self):
        self.api.authenticate()
        stock_price = self.api.get_apple_stock_price()
        if stock_price >= 100:
            self.api.place_order(side='buy', symbol=self.symbol, quantity=1, price=stock_price)
            
    def run(self):
        """
        Runs the automated trading program.
        """
        # Get the initial stock price
        current_price = self.get_stock_price()

        # Keep track of the previous price
        previous_price = current_price

        # Loop indefinitely
        while True:
            # Get the current price
            current_price = self.get_stock_price()

            # If the price has changed, print the new price
            if current_price != previous_price:
                print(f'Current price: {current_price}')

            # Update the previous price
            previous_price = current_price

            # Check if the current price is at the target price
            if current_price >= self.target_price:
                # Place a buy order for one share of the stock
                order = self.api.place_order(order_side='buy', symbol=self.symbol, quantity=1, price=current_price)


                # Print the order details
                print(f'Buy order placed: {order}')

            # Wait for a short time before checking the price again
            time.sleep(1)

    def get_stock_price(self):
        """
        Returns the current price of the specified stock symbol.
        """
        # Replace this with code to retrieve the current price from the API
        # For now, we will return a random price between 90 and 110
        return random.uniform(90, 110)
