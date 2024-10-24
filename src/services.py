import json
import logging
import re

from src.views import get_excel

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def find_numbers(list_transactions):
    current_transactions = []
    phone_pattern = re.compile(r"\+?\d{1,3}\s*\d{1,3}[\s-]?\d{2}[\s-]?\d{2}[\s-]?\d{2}")
    for transaction in list_transactions:
        description = transaction.get("Описание", "")
        if phone_pattern.search(description):
            current_transactions.append(transaction)
    logger.debug("Correct returned phone numbers in description")
    current_transactions = json.dumps(current_transactions, ensure_ascii=False)
    return current_transactions


# print(find_numbers(get_excel("dict")))
