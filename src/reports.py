import functools
from datetime import datetime
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta

from src.utils import get_excel


import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "a")
file_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def report_decorator(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as f:
                f.write(f"{result}\n")
            return result

        return wrapper

    return decorator


def date_now():
    """Функция, возвращающая текущую дату"""
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.2021")
    return formatted_date


@report_decorator("report.txt")
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = date_now()
):
    """Функция, возвращающая список транзакций по заданной категории за 3 месяца"""
    if date is None:
        return []

    date_format = "%d.%m.%Y"
    end_date = datetime.strptime(date, date_format)
    start_date = end_date - relativedelta(months=3)

    current_transactions = []
    for index, transaction in transactions.iterrows():
        if not isinstance(transaction["Дата платежа"], str):
            continue
        transaction_date = datetime.strptime(transaction["Дата платежа"], date_format)
        if (
            transaction["Категория"] == category
            and start_date <= transaction_date <= end_date
        ):
            current_transactions.append(transaction.to_dict())
    logger.debug(f'Correct returned spending by category {category}')
    return current_transactions


# print(*spending_by_category(get_excel('dataframe'), "Каршеринг", '17.12.2021'), sep='\n')
