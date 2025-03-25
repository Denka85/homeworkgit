import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from typing import List, Dict

class TestFilterByCurrency:
    @pytest.fixture
    def sample_transactions(self) -> List[Dict]:
        return [
            {'operationAmount': {'currency': {'code': 'USD'}}},
            {'operationAmount': {'currency': {'code': 'EUR'}}},
            {'operationAmount': {'currency': {'code': 'USD'}}},
            {'invalid': 'data'},
            {}
        ]

    def test_filters_correctly(self, sample_transactions):
        result = list(filter_by_currency(sample_transactions, 'USD'))
        assert len(result) == 2
        assert all(t['operationAmount']['currency']['code'] == 'USD' for t in result)

    def test_empty_input(self):
        assert list(filter_by_currency([], 'USD')) == []

class TestTransactionDescriptions:
    @pytest.fixture
    def sample_transactions(self) -> List[Dict]:
        return [
            {'description': 'Payment 1'},
            {'description': 'Payment 2'},
            {'no_desc': 'test'},
            {}
        ]

    def test_yields_descriptions(self, sample_transactions):
        result = list(transaction_descriptions(sample_transactions))
        assert result == ['Payment 1', 'Payment 2', None, None]

class TestCardNumberGenerator:
    def test_generates_correct_range(self):
        result = list(card_number_generator(1, 4))
        assert result == [
            '0000 0000 0000 0001',
            '0000 0000 0000 0002',
            '0000 0000 0000 0003'
        ]

    def test_formats_correctly(self):
        num = next(card_number_generator(1234567890123456, 1234567890123457))
        assert num == '1234 5678 9012 3456'