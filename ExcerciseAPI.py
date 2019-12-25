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
    return coinBaseTick.json()['data']['amount']


def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', data=json.dumps({"pair": "XXBTZUSD"}),
                               headers={'content-type': 'application/json'})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]


# get last btcusd bid and ask orders from bitstamp orderbook
# bid
def btstampOrderBookLastBidPrice():
    bitStampOrderBookLastBidPrice = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampOrderBookLastBidPrice.json()['bids'][0][0]


def btstampOrderBookLastBidQuantity():
    bitStampOrderBookLastBidQuantity = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampOrderBookLastBidQuantity.json()['bids'][0][1]


# ask
def btstampOrderBookLastAskPrice():
    bitStampOrderBookLastAskPrice = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampOrderBookLastAskPrice.json()['asks'][1][0]


def btstampOrderBookLastAskQuantity():
    bitStampOrderBookLastAskQuantity = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd')
    return bitStampOrderBookLastAskQuantity.json()['asks'][1][1]


def main():
    #    from argparse import ArgumentParser

    #    parser = ArgumentParser()
    #    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    #    args = parser.parse_args()

    #    app.run(host='0.0.0.0', port=args.port)
    # response = btstamp()
    # print(response)
    # response = bitfinex()
    # print(response)
    while True:
        btstampUSDLive = float(btstamp())
        coinbUSDLive = float(coinbase())
        krakenUSDLive = float(kraken())
        bitfinexUSDLive = float(bitfinex())

        print(" --- ticker ---")
        print("Bitstamp Price in USD =", btstampUSDLive)
        print("Coinbase Price in USD =", coinbUSDLive)
        print("Kraken Price in USD =", krakenUSDLive)
        print("Bitfinex Price in USD =", bitfinexUSDLive)
        print(" ")

        btstampOrderBookLastBidP = float(btstampOrderBookLastBidPrice())
        btstampOrderBookLastBidQ = float(btstampOrderBookLastBidQuantity())
        btstampOrderBookLastAskP = float(btstampOrderBookLastAskPrice())
        btstampOrderBookLastAskQ = float(btstampOrderBookLastAskQuantity())

        print(" --- bitstamp BTCUSD orders ---")
        print("last bid:")
        print("         price =", btstampOrderBookLastBidP)
        print("         quantity =", btstampOrderBookLastBidQ)
        print("last ask:")
        print("         price =", btstampOrderBookLastAskP)
        print("         quantity =", btstampOrderBookLastAskQ)
        print(" ")
        print(" ")
        print(" ")
        time.sleep(3)  # 120 equals two minutes


if __name__ == "__main__":
    print("Started...")
    main()
