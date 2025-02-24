import pytest


@pytest.fixture
def dictionary_list() -> list[dict[str, str]]:
    return [
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": "123456789", "state": "EXECUTED", "date": "2023-01-15T12:34:56.789012"},
        {"id": "987654321", "state": "CANCELED", "date": "2022-11-22T08:45:10.123456"},
        {"id": "456789123", "state": "EXECUTED", "date": "2021-05-10T14:20:30.456789"},
        {"id": "321654987", "state": "CANCELED", "date": "2020-09-05T19:55:25.987654"},
        {"id": "789123456", "state": "EXECUTED", "date": "2019-12-31T23:59:59.000001"},
        {"id": "654987321", "state": "CANCELED", "date": "2018-03-18T06:15:45.654321"},
    ]


@pytest.fixture
def dictionary_list_true() -> list[dict[str, str]]:
    return [
        {"id": "123456789", "state": "EXECUTED", "date": "2023-01-15T12:34:56.789012"},
        {"id": "987654321", "state": "CANCELED", "date": "2022-11-22T08:45:10.123456"},
        {"id": "456789123", "state": "EXECUTED", "date": "2021-05-10T14:20:30.456789"},
        {"id": "321654987", "state": "CANCELED", "date": "2020-09-05T19:55:25.987654"},
        {"id": "789123456", "state": "EXECUTED", "date": "2019-12-31T23:59:59.000001"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "654987321", "state": "CANCELED", "date": "2018-03-18T06:15:45.654321"},
    ]


@pytest.fixture
def dictionary_list_false() -> list[dict[str, str]]:
    return [
        {"id": "654987321", "state": "CANCELED", "date": "2018-03-18T06:15:45.654321"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": "789123456", "state": "EXECUTED", "date": "2019-12-31T23:59:59.000001"},
        {"id": "321654987", "state": "CANCELED", "date": "2020-09-05T19:55:25.987654"},
        {"id": "456789123", "state": "EXECUTED", "date": "2021-05-10T14:20:30.456789"},
        {"id": "987654321", "state": "CANCELED", "date": "2022-11-22T08:45:10.123456"},
        {"id": "123456789", "state": "EXECUTED", "date": "2023-01-15T12:34:56.789012"},
    ]


@pytest.fixture
def transactions() -> list[dict]:
    transactions_data: list[dict] = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions_data
