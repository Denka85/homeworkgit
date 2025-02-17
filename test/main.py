from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    card_num = 7000792289606361
    account_num = 73654108430135874305

    print("Маска карты:", get_mask_card_number(card_num))
    print("Маска счета:", get_mask_account(account_num))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
