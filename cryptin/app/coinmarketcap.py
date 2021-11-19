import requests
from kafka import KafkaProducer
import json
import os

# global variables
api_key = ''
#bot_token = 'your_telegram_bot_token'
#chat_id = 'your_telegram_account_chat_id_here'
threshold = 30000
producer = KafkaProducer(bootstrap_servers='192.168.0.112')
print(os.environ.get('bootstrap_servers'))

def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.environ.get('coinmarketcap')
    }

    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()
#    print(response_json)
    # extract the bitcoin price from the json data
    for coin in response_json["data"]:
        roin = {}
        roin["name"] = coin["name"]
        roin["max_supply"] = coin["max_supply"]
        roin["circulating_supply"] = coin["circulating_supply"]
        roin["total_supply"] = coin["total_supply"]
        roin["platform"] = coin["platform"]
        roin["cmc_rank"] = coin["cmc_rank"]
        roin["last_updated"] = coin["last_updated"]
        roin["price"] = coin["quote"]["USD"]["price"]
        roin["volume_24h"] = coin["quote"]["USD"]["volume_24h"]
        roin["percent_change_1h"] = coin["quote"]["USD"]["percent_change_1h"]
        roin["percent_change_24h"] = coin["quote"]["USD"]["percent_change_24h"]
        roin["percent_change_7d"] = coin["quote"]["USD"]["percent_change_7d"]
        roin["percent_change_30d"] = coin["quote"]["USD"]["percent_change_30d"]
        roin["percent_change_60d"] = coin["quote"]["USD"]["percent_change_60d"]
        roin["percent_change_90d"] = coin["quote"]["USD"]["percent_change_90d"]
        roin["market_cap"] = coin["quote"]["USD"]["market_cap"]
        roin["last_updated"] = coin["quote"]["USD"]["last_updated"]
        send_message(roin)
    
    
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']

# fn to send_message through te
# legram

def send_message(msg):
    print(msg)
    producer.send("coin",key=bytes(str(3), encoding='utf-8'),value=bytes(json.dumps(msg), encoding='utf-8'))
def main():
    price_list = []

    price = get_btc_price()
    price_list.append(price)

    # if the price falls below threshold, send an immediate msg
    if price < threshold:
        print(f'BTC Price Drop Alert: {price}')
    else:
        print(f'BTC Price: {price}')


if __name__ == '__main__':
    main()