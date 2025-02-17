import pytest

from src.processing import filter_by_state, sort_by_date, LengthListError


def test_filter_by_state_execute(dictionary_list):
    result = filter_by_state(dictionary_list, state="EXECUTE")
    for key in result:
        assert key["state"] == "EXECUTE"

    result = filter_by_state(dictionary_list, state="CANCELED")
    for key in result:
        assert key["state"] == "CANCELED"

    result = filter_by_state(dictionary_list, state=" ")
    assert len(result) == 0


@pytest.mark.parametrize("date, expected_fixture_name",
                         [
                             (True, "dictionary_list_true"),
                             (False, "dictionary_list_false")
                         ]
                         )
def test_sort_by_date(request, dictionary_list, date, expected_fixture_name):
    expected_output = request.getfixturevalue(expected_fixture_name)
    assert sort_by_date(dictionary_list, date) == expected_output

    # Функция
# sort_by_date
# :
# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
# Проверка корректности сортировки при одинаковых датах.
# Тесты на работу функции с некорректными или нестандартными форматами дат.
