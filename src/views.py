import datetime
import pandas as pd
from user_settings_json import add_to_list


def hello(current_time):
    '''Функция приветствия, возвращающая соответствующее сообщение в зависимости от времени суток.'''
    current_time = datetime.datetime.strptime(current_time, "%d.%m.%Y %H:%M:%S")
    current_time = current_time.time()
    night_end = datetime.time(2, 59, 59)
    morning_start = datetime.time(5, 0, 0)
    morning_end = datetime.time(11, 59, 59)
    evening_start = datetime.time(17, 0, 0)
    evening_end = datetime.time(23, 59, 59)
    if current_time <= night_end:
        return 'Доброй ночи!'
    elif morning_start <= current_time <= morning_end:
        return 'Доброе утро!'
    elif evening_start <= current_time <= evening_end:
        return 'Добрый вечер!'
    else:
        return 'Добрый день!'


# print(hello('18.12.2021 16:53:16'))


def get_json_excel():
    get_excel_file = pd.read_excel('../data/operations.xlsx')
    dict_exl = get_excel_file.to_dict(orient="records")
    return dict_exl


# print(get_json_excel())


def generate_json(current_date):
    current_transactions = []
    for transaction in get_json_excel():
        if str(transaction['Дата платежа'])[2:] == current_date[2:10] and str(transaction['Дата платежа'])[:2] <= current_date[:2]:
            current_transactions.append(transaction)
    cards = []
    top_transactions = []
    filtered_transactions = [{'greeting': hello(current_date)}]
    for transaction_2 in current_transactions:
        card = {'last_digit': transaction_2['Номер карты'], 'total_spent': transaction_2['Сумма операции'], 'cashback': round(transaction_2['Сумма операции'] / 100, 2)}
        cards.append(card)
        top = {'date': transaction_2['Дата платежа'], 'amount': transaction_2['Сумма платежа'], 'category': transaction_2['Категория'], 'description': transaction_2['Описание']}
        top_transactions.append(top)
    filtered_transactions[0]['cards'] = cards
    top_transactions.sort(key=lambda x: x['amount'])
    filtered_transactions[0]['top_transactions'] = top_transactions
    filtered_transactions[0]['currency_rates'] = add_to_list()
    print(current_transactions)
    print()
    return filtered_transactions


print(generate_json('01.11.2021 5:50:17'), sep='\n')

