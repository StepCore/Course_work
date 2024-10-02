import pytest


@pytest.fixture
def top_transactions():
    """from 04.11.2021 23:50:17"""
    return [
        {
            "date": "03.11.2021",
            "amount": 10000.0,
            "category": "Другое",
            "description": "Иван С.",
        },
        {
            "date": "02.11.2021",
            "amount": 5510.8,
            "category": "Каршеринг",
            "description": "Ситидрайв",
        },
        {
            "date": "01.11.2021",
            "amount": 525.0,
            "category": "Одежда и обувь",
            "description": "WILDBERRIES",
        },
        {
            "date": "04.11.2021",
            "amount": 395.92,
            "category": "Супермаркеты",
            "description": "Магнит",
        },
        {
            "date": "04.11.2021",
            "amount": 290.01,
            "category": "Косметика",
            "description": "Подружка",
        },
    ]


@pytest.fixture
def generate_all_transactions():
    """from 01.11.2021 23:50:17"""
    return [
        {
            "Дата операции": "01.11.2021 15:32:24",
            "Дата платежа": "01.11.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -228.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -228.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 11.0,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 11,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 228.0,
        },
        {
            "Дата операции": "01.11.2021 11:01:19",
            "Дата платежа": "01.11.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -110.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -110.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 1.0,
            "Категория": "Фастфуд",
            "MCC": 5814.0,
            "Описание": "Mouse Tail",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 110.0,
        },
        {
            "Дата операции": "31.10.2021 19:06:21",
            "Дата платежа": "01.11.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -525.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -525.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 26.0,
            "Категория": "Одежда и обувь",
            "MCC": 5651.0,
            "Описание": "WILDBERRIES",
            "Бонусы (включая кэшбэк)": 26,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 525.0,
        },
    ]
