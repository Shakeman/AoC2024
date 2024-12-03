from Day.day2 import day_2_part_1, day_2_part_2


def test_day2_part1() -> None:
    test_reports: list[list[int]] = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert day_2_part_1(test_reports) == 2


def test_day2_part2() -> None:
    test_reports: list[list[int]] = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert day_2_part_2(test_reports) == 4
