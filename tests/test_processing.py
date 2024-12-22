




def test_filter_by_state(test_dict_list_correct_date):
    assert filter_by_state(test_dict_list_correct_date) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30'}]


def test_filter_by_state(test_dict_list_not_correct_date):
    assert filter_by_state(test_dict_list_not_correct_date) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': 'asdasdf'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '********'}]


def test_sort_by_date(test_dict_list):
    assert sort_by_date(test_dict_list) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]