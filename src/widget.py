from masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер, сохраняя название карты/счета"""
    if info.startswith("Счет"):
        account_number = info[5:]
        masked_account = get_mask_account(account_number)
        if masked_account == "Неверный номер счета":
            return "Неверный номер счета или карты"
        return f"Счет {masked_account}"
    else:
        separate = info.split()
        name = " ".join(separate[:-1])
        card_number = separate[-1]
        masked_card = get_mask_card_number(card_number)
        if masked_card == "Неверный номер карты":
            return "Неверный номер счета или карты"
        return f"{name} {masked_card}"


def get_date(date_str: str) -> str:
    """Преобразует формат даты"""
    try:
        date_separate = date_str.split("T")[0]
        year, month, day = date_separate.split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        return "Неверный формат даты"


if __name__ == "__main__":
    user_input_info = input("Введите данные карты или счета: ")
    print(mask_account_card(user_input_info))
    user_input_date = input("Введите дату: ")
    print(get_date(user_input_date))
