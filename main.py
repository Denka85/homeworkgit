from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def test_get_mask_card_number():
    card_number = 7000792289606361
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"

def test_get_mask_account():
    account_number = 73654108430135874305
    assert get_mask_account(account_number) == "**4305"
    '''данные для маскировки номера карт и аккаунта'''
    card_num = 7000792289606361
    account_num = 73654108430135874305

    '''вывод маски карт и даты'''
    print("Маска карты:", get_mask_card_number(card_num))
    print("mainМаска счета:", get_mask_account(account_num))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))

'''список словарей для фильтра для модуля processing'''
operations_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
