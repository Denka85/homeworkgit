import pytest
from src.widget import get_date, mask_account_card

def test_mask_account_card(input_card_info, expected_output):
    if expected_output == ValueError:
        with pytest.raises(ValueError):
            mask_account_card(input_card_info)
    else:
        result = mask_account_card(input_card_info)
        assert result == expected_output


def test_get_date(input_date, expected_output):
    if expected_output == ValueError:
        with pytest.raises(ValueError):
            get_date(input_date)
    else:
        result = get_date(input_date)
        assert result == expected_output
