import datetime

from src.utils import get_excel, generate_json, filtered_cards, filtered_top, cards, top_list
from user_settings_json import add_to_list, get_current_stock, settings


def hello(current_time):
    """Функция приветствия, возвращающая соответствующее сообщение в зависимости от времени суток."""
    try:
        current_time = datetime.datetime.strptime(current_time, "%d.%m.%Y %H:%M:%S")
    except ValueError:
        raise ValueError("Некорректный формат времени")
    current_time = current_time.time()
    night_end = datetime.time(2, 59, 59)
    morning_start = datetime.time(5, 0, 0)
    morning_end = datetime.time(11, 59, 59)
    evening_start = datetime.time(17, 0, 0)
    evening_end = datetime.time(23, 59, 59)
    if current_time <= night_end:
        return "Доброй ночи!"
    elif morning_start <= current_time <= morning_end:
        return "Доброе утро!"
    elif evening_start <= current_time <= evening_end:
        return "Добрый вечер!"
    else:
        return "Добрый день!"


transaction_for_print = [{}]


def final_list(current_date):
    """Функция, формирующая конечный список из готовых данных"""
    generate_json(current_date)
    filtered_cards()
    filtered_top()
    transaction_for_print[0]["greeting"] = hello(current_date)
    transaction_for_print[0]["cards"] = cards
    transaction_for_print[0]["top_transactions"] = top_list
    transaction_for_print[0]["currency_rates"] = add_to_list()
    transaction_for_print[0]["stock_prices"] = get_current_stock(settings)
    return transaction_for_print


print(final_list("01.11.2021 23:50:17"), sep="\n")
