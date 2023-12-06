from flask import Flask, render_template
from flask import jsonify
import requests

app = Flask(__name__)

def BitCoin_Price():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    return data['price']

@app.route("/")
def BTC():
    return render_template("index.html")

@app.route("/get_btc_price")
def get_btc_price():
    btc_price = BitCoin_Price()
    return jsonify({"btc_price": btc_price})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2080)
