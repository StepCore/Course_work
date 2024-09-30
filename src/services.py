from views import get_dataframe_excel


def find_numbers(num):
    current_transactions = []
    for transaction in get_dataframe_excel():
        if num in transaction["Описание"]:
            current_transactions.append(transaction)
    return current_transactions


# print(*find_numbers('98'), sep='\n')
