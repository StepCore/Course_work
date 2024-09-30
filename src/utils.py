import pandas as pd


def get_dataframe_excel():
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    return get_excel_file


# print(get_json_excel())
