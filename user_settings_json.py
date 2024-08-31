import requests


def get_current_price():
    url = "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=RUB&amount={1}"

    payload = {}
    headers = {
        "apikey": "jqhlspps8Cks9V3f4XwGI5qZrXx5gcpj"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.text
    return result


print(get_current_price())
