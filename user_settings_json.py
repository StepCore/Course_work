import requests


settings = {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}
currency_list = []


def get_current_price(currency):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount=1"

    payload = {}
    headers = {
        "apikey": "jqhlspps8Cks9V3f4XwGI5qZrXx5gcpj"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    user_currencies = response.json()['query']['from']
    price = response.json()['info']['rate']
    price = round(price, 2)

    return {'currency': user_currencies, 'rate': price}


# print(get_current_price('USD'))


def add_to_list():
    for currency in settings['user_currencies']:
        currency_list.append(get_current_price(currency))
    return currency_list


# print(add_to_list())
