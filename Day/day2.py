import itertools
from pathlib import Path


def read_input(file_path: Path) -> list[list[int]]:
    list_of_reports: list[list[int]] = []
    with file_path.open() as file:
        for line in file:
            report: list[int] = list(map(int, line.split()))
            list_of_reports.append(report)
    return list_of_reports

def safety_test_1(deltas: list[int]) -> bool:
    return all(x > 0 for x in deltas) or all(x < 0 for x in deltas)

def safety_test_2(deltas: list[int]) -> bool:
    absolute_deltas = [abs(num) for num in deltas]
    return max(absolute_deltas) < 4  # noqa: PLR2004

def day_2_part_1(reports: list[list[int]]) -> int:
    safe_reports: list[bool] = []
    for report in reports:
        deltas: list[int] = [b-a for a,b in itertools.pairwise(report)]
        pass_test_1: bool = safety_test_1(deltas)
        pass_test_2: bool = safety_test_2(deltas)
        safe_reports.append(pass_test_1 and pass_test_2)
    return sum(safe_reports)
file_path: Path = Path.cwd() / "Input" / "day2.txt"
reports: list[list[int]] = read_input(file_path)
print(day_2_part_1(reports))
