import time, json, requests


# get tickets from various exchanges
def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last']  # experiment replace last with other values


def bitfinex():
    bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')
    return bitFinexTick.json()['last_price']


def coinbase():
    coinBaseTick = requests.get('https://coinbase.com/api/v2/prices/BTC-USD/buy')
    return coinBaseTick.json()['date']['amount']


def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', data=json.dumps({"pair": "XXBTZUSD"}),
                               headers={'content-type': 'application/json'})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]

# get last btcusd bid and ask orders from bitstamp orderbook
# bid
def bistampOrderBookLastBidPrice():
    bitStampOrderBookLastBidPrice = requests.get('https://www.bitstamp.net/api/v2/order_book/btcsud/')
    return bitStampOrderBookLastBidPrice.json()['bids']['0']['0']


def main():
    #    from argparse import ArgumentParser

    #    parser = ArgumentParser()
    #    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    #    args = parser.parse_args()

    #    app.run(host='0.0.0.0', port=args.port)
    response = btstamp()
    print(response)
    response = bitfinex()
    print(response)


if __name__ == "__main__":
    print("Started...")
    main()
