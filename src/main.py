"-*- coding: utf-8 -*-"
import datetime

from src.reports import spending_by_category
from src.services import find_numbers
from src.views import final_list, get_excel


def banking_application():
    """Функция, связывающая все задачи проекта"""
    user_answer = input(
        "Выберите категорию из доступных:\n1. Главная\n2. Поиск по телефонным номерам\n3. Траты по категории\n"
    )
    if user_answer.lower() == "главная" or user_answer == "1":
        print('Введите корректную дату и время в формате "ДД.ММ.ГГГГ ЧЧ:ММ:СС".')
        user_answer = input()
        try:
            datetime_format = datetime.datetime.strptime(user_answer, "%d.%m.%Y %H:%M:%S")
            if isinstance(datetime_format, datetime.datetime):
                user_answer = final_list(user_answer)
            else:
                return "Неверный формат данных"
        except ValueError:
            return "Неверный формат данных"
    elif user_answer.lower() == "поиск по телефонным номерам" or user_answer == "2":
        user_answer = find_numbers(get_excel("dict"))
    elif user_answer.lower() == "траты по категории" or user_answer == "3":
        print("Введите категорию для поиска")
        user_category = input()
        print('Введите дату для поиска транзакций за 3 месяца в формате: "ДД.ММ.ГГГГ".')
        user_date = input()
        user_answer = spending_by_category(get_excel("dataframe"), user_category, user_date)
    else:
        return "Неизвестная категория"

    return user_answer


print(banking_application())
