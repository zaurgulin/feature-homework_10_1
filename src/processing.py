from typing import Dict, List, Any

origin_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED"):
    """Функция фильтрации операций по ключу state"""
    new_data = []
    for operation in data:
       if operation["state"] == state:
           new_data.append(operation)
    return new_data

print(filter_by_state(origin_list))



def sort_by_date(data: List[Dict[str, Any]], order: bool = True):
    """Функция фильтрации операций по дате"""
    sorted_data = sorted(data, key=lambda k: k["date"], reverse=order)
    return sorted_data

print(sort_by_date(origin_list))
