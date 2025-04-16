import json

import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


@patch("builtins.open", mock_open(read_data='[{"id": 1}]'))
def test_load_transactions_success():
    assert load_transactions("dummy.json") == [{"id": 1}]

def test_load_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data='')):
        assert load_transactions("empty.json") == []

@pytest.mark.parametrize("content, expected", [
    ('[{"id": 1}]', [{"id": 1}]),
    ('[]', []),
    ('', []),
    ('{"id": 1}', []),
])
def test_load_transactions(content, expected):
    with patch("builtins.open", mock_open(read_data=content)), \
         patch("json.load", return_value=json.loads() if content else {}):
        assert load_transactions("dummy_path") == expected