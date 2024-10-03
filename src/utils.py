import pandas as pd


def get_excel(formatting):
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    if formatting == "dataframe":
        return get_excel_file
    elif formatting == "dict":
        return get_excel_file.to_dict(orient="records")
    else:
        raise ValueError("Invalid format specified. Use 'dataframe' or 'dict'.")


# print(get_excel('dataframe'))
