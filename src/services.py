from src.views import get_excel
import json

import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "a")
file_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def find_numbers(list_transactions):
    current_transactions = []
    for transaction in list_transactions:
        if '+' in transaction["Описание"]:
            current_transactions.append(transaction)
    logger.debug('Correct returned phone numbers in description')
    current_transactions = json.dumps(current_transactions, ensure_ascii=False)
    return current_transactions


print(find_numbers(get_excel("dict")))
