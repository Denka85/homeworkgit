from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions


@patch("builtins.open", mock_open(read_data='[{"id": 1}]'))
def test_load_transactions_success():
    assert load_transactions("dummy.json") == [{"id": 1}]

def test_load_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data='')):
        assert load_transactions("empty.json") == []