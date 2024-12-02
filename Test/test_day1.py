from Day.day1 import day_1_part_1, day_1_part_2


def test_day1() -> None:
    test_list_1: list[int] = [3, 4, 2, 1, 3, 3]
    test_list_2: list[int] = [4, 3, 5, 3, 9, 3]
    assert day_1_part_1(test_list_1, test_list_2) == 11

def test_day1_part2() -> None:
    test_list_1: list[int] = [3, 4, 2, 1, 3, 3]
    test_list_2: list[int] = [4, 3, 5, 3, 9, 3]
    assert day_1_part_2(test_list_1, test_list_2) == 31
