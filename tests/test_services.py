"-*- coding: utf-8 -*-"

import json

import pytest

from src.services import find_numbers


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            [
                {"Описание": "Оплата за услуги +7 123 45 67"},
                {"Описание": "Без номера телефона"},
                {"Описание": "Контакт: +1 800 555 35 12"},
            ],
            json.dumps(
                [{"Описание": "Оплата за услуги +7 123 45 67"}, {"Описание": "Контакт: +1 800 555 35 12"}],
                ensure_ascii=False,
            ),
        ),
        (
            [{"Описание": "Транзакция без телефона"}, {"Описание": "Звонок на номер +44 20 1234 5678"}],
            json.dumps([{"Описание": "Звонок на номер +44 20 1234 5678"}], ensure_ascii=False),
        ),
        (
            [{"Описание": "Неверный формат номера 123-456"}, {"Описание": "+7 495 123-45-67"}],
            json.dumps([{"Описание": "+7 495 123-45-67"}], ensure_ascii=False),
        ),
        ([], json.dumps([], ensure_ascii=False)),
    ],
)
def test_find_numbers(input_data, expected_output):
    assert find_numbers(input_data) == expected_output
