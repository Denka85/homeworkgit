from unittest.mock import patch
from src.external_api import convert_to_rub

@patch('requests.get')
def test_convert_usd(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {'rates': {'RUB': 75.5}}
    transaction = {'amount': 100, 'currency': 'USD'}
    assert convert_to_rub(transaction) == 7550.0