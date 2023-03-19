import threading
import time

from trader import Trader
from brokerApi import MockAPI

def start_trading():
    api = MockAPI('https://paper-api.alpaca.markets', 'api_key', 'api_secret')
    trader = Trader(api)
    trader.start()

    # Wait for user input to stop the app
    while True:
        user_input = input()
        if user_input == 'stop':
            trader.stop()
            print('Trading app stopped.')
            break

if __name__ == '__main__':
    print('Starting trading app...')
    start_trading()
