from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    card_number = 7000792289606361
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_account():
    account_number = 73654108430135874305
    assert get_mask_account(account_number) == "**4305"
