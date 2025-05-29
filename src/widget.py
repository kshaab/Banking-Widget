from masks import get_mask_account, get_mask_card_number

user_input_info = input()


def mask_account_card(info: str) -> str:
    if info.startswith("Счет"):
        account_number = info[5:]
        return f"Счет {get_mask_account(account_number)}"
    else:
        separate = info.split()
        name = " ".join(separate[:-1])
        card_number = separate[-1]
        return f"{name} {get_mask_card_number(card_number)}"


if __name__ == "__main__":
    print(mask_account_card(user_input_info))

