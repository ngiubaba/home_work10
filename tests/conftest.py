import pytest


@pytest.fixture
def dictionary_list():
    return [
        {'id': "594226727", 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': "615064591", 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': "123456789", 'state': 'EXECUTED', 'date': '2023-01-15T12:34:56.789012'},
        {'id': "987654321", 'state': 'CANCELED', 'date': '2022-11-22T08:45:10.123456'},
        {'id': "456789123", 'state': 'EXECUTED', 'date': '2021-05-10T14:20:30.456789'},
        {'id': "321654987", 'state': 'CANCELED', 'date': '2020-09-05T19:55:25.987654'},
        {'id': "789123456", 'state': 'EXECUTED', 'date': '2019-12-31T23:59:59.000001'},
        {'id': "654987321", 'state': 'CANCELED', 'date': '2018-03-18T06:15:45.654321'}
    ]

@pytest.fixture
def dictionary_list_true():
    return [
        {'id': "123456789", 'state': 'EXECUTED', 'date': '2023-01-15T12:34:56.789012'},
        {'id': "987654321", 'state': 'CANCELED', 'date': '2022-11-22T08:45:10.123456'},
        {'id': "456789123", 'state': 'EXECUTED', 'date': '2021-05-10T14:20:30.456789'},
        {'id': "321654987", 'state': 'CANCELED', 'date': '2020-09-05T19:55:25.987654'},
        {'id': "789123456", 'state': 'EXECUTED', 'date': '2019-12-31T23:59:59.000001'},
        {'id': "615064591", 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': "594226727", 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': "654987321", 'state': 'CANCELED', 'date': '2018-03-18T06:15:45.654321'}
    ]

@pytest.fixture
def dictionary_list_false():
    return [
        {'id': "654987321", 'state': 'CANCELED', 'date': '2018-03-18T06:15:45.654321'},
        {'id': "594226727", 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': "615064591", 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': "789123456", 'state': 'EXECUTED', 'date': '2019-12-31T23:59:59.000001'},
        {'id': "321654987", 'state': 'CANCELED', 'date': '2020-09-05T19:55:25.987654'},
        {'id': "456789123", 'state': 'EXECUTED', 'date': '2021-05-10T14:20:30.456789'},
        {'id': "987654321", 'state': 'CANCELED', 'date': '2022-11-22T08:45:10.123456'},
        {'id': "123456789", 'state': 'EXECUTED', 'date': '2023-01-15T12:34:56.789012'}
    ]