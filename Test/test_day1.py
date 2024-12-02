from Day.day1 import day_1_process

def test_day1() -> None:
    test_list_1: list[int] = [3, 4, 2, 1, 3, 3]
    test_list_2: list[int] = [4, 3, 5, 3, 9, 3]
    assert day_1_process(test_list_1, test_list_2) == 11