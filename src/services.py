from views import get_json_excel


def find_numbers(num):
    current_transactions = []
    for transaction in get_json_excel():
        if num in transaction["Описание"]:
            current_transactions.append(transaction)
    return current_transactions


print(*find_numbers('98'), sep='\n')
