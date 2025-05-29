def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    card_number_str = str(card_number).replace(" ", "")
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        return "Неверный номер карты"

    first_six_digits = card_number_str[0:6]
    last_four_digits = card_number_str[-4:]

    masked_card_number = first_six_digits[:4] + " " + first_six_digits[4:6] + "** ****" + " " + last_four_digits
    return masked_card_number


def get_mask_account(account: str) -> str:
    """Функция маскирует номер счета"""
    account_str = str(account).replace(" ", "")
    if len(account_str) != 20 or not account_str.isdigit():
        return "Неверный номер счета"

    last_four_digits = account_str[-4:]

    masked_account = "**" + last_four_digits
    return masked_account


if __name__ == "__main__":
    user_input_card_number = input("Введите номер карты: ")
    print(get_mask_card_number(user_input_card_number))

    user_input_account = input("Введите номер счета: ")
    print(get_mask_account(user_input_account))
