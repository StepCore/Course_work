import pandas as pd
from views import hello


def get_json_excel():
    get_excel_file = pd.read_excel('../data/operations.xlsx')
    dict_exl = get_excel_file.to_dict(orient="records")
    return dict_exl


# print(get_json_excel())
