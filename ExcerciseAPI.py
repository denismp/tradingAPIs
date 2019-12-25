import time, json, requests


# get tickets from various exchanges
def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last']  # experiment replace last with other values


def main():
    #    from argparse import ArgumentParser

    #    parser = ArgumentParser()
    #    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    #    args = parser.parse_args()

    #    app.run(host='0.0.0.0', port=args.port)
    json = btstamp()
    print(json)


if __name__ == "__main__":
    print("Started...")
    main()
