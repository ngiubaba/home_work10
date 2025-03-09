from unittest.mock import Mock, patch

from src.external_api import convert_rub


def test_convert_amount() -> None:
    """Тест функции по конвертации из любой валюты в рубли"""

    mock_response = Mock()
    mock_response.json.return_value = {
        "result": 870.0
    }

    # Мокаем requests.request
    with patch('requests.request', return_value=mock_response):
        result = convert_rub("USD", 10)
        assert result == 870.0