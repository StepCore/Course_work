import numpy
import pandas as pd


def get_excel(formatting):
    current_transaction = []
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    if formatting == "dataframe":
        return get_excel_file
    elif formatting == "dict":
        for transaction in get_excel_file.to_dict(orient="records"):
            transaction = {
                key: (
                    None if isinstance(value, float) and numpy.isnan(value) else value
                )
                for key, value in transaction.items()
            }
            current_transaction.append(transaction)
        return current_transaction
    else:
        raise ValueError("Invalid format specified. Use 'dataframe' or 'dict'.")


# print(get_excel('dict'))

current_transactions = []
cards = []
top_list = []


def generate_json(current_date):
    """Функция, возвращающая отфильтрованные по дате транзакции"""
    for transaction in get_excel("dict"):
        if (
            str(transaction["Дата платежа"])[2:10] == current_date[2:10]
            and str(transaction["Дата платежа"])[:2] <= current_date[:2]
        ):
            current_transactions.append(transaction)
    return current_transactions


def filtered_cards():
    """Функция, возвращающая правильный список карт"""
    for transaction in current_transactions:
        card = {
            "last_digit": transaction["Номер карты"],
            "total_spent": transaction["Сумма операции"],
            "cashback": round(transaction["Сумма операции"] / 100, 2),
        }
        cards.append(card)
    return cards


def filtered_top():
    """Функция, возвращающая топ 5 транзакций по платежам"""
    sort_current_transactions = sorted(
        current_transactions, reverse=True, key=lambda x: abs(x["Сумма платежа"])
    )
    for transaction in sort_current_transactions:
        top = {
            "date": transaction["Дата платежа"],
            "amount": abs(transaction["Сумма платежа"]),
            "category": transaction["Категория"],
            "description": transaction["Описание"],
        }
        top_list.append(top)
        if len(top_list) == 5:
            break
    return top_list