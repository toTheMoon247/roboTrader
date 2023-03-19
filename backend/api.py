from flask import Flask
from trader import Trader

app = Flask(__name__)
trader = Trader()

@app.route('/start')
def start():
    trader.start()
    return 'Trading app started'

@app.route('/stop')
def stop():
    trader.stop()
    return 'Trading app stopped'
