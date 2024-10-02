from src.views import final_list, generate_json


def test_greeting():
    assert final_list("04.11.2021 23:50:17")[0]["greeting"] == "Добрый вечер!"


def test_top_transactions(top_transactions):
    assert final_list("04.11.2021 23:50:17")[0]["top_transactions"] == top_transactions


def test_generate_json(generate_all_transactions):
    assert generate_json("01.11.2021 23:50:17") == generate_all_transactions
