def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по ключу"""
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(info: list[dict], reverse: bool = True) -> list[dict]:
    """Фильтрует список словарей по дате"""
    sorted_info = sorted(info, key=lambda item: item.get("date", ""), reverse=reverse)
    return sorted_info


if __name__ == "__main__":
    dict_list = [
        {"id": 1428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    user_state = input("Введите значение для фильтрации: ")
    if not user_state:
        user_state = "EXECUTED"
    print(filter_by_state(dict_list, user_state))

    info_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(info_list, reverse=True))
