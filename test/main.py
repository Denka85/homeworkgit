from src.masks import get_mask_account, get_mask_card_number


if __name__ == "__main__":
    card_num = 7000792289606361
    account_num = 73654108430135874305

    print("Маска карты:", get_mask_card_number(card_num))
    print("Маска счета:", get_mask_account(account_num))

