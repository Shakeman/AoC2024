import itertools
from pathlib import Path
import re


def read_input(file_path: Path) -> list[list[int]]:
    list_of_reports: list[list[int]] = []
    with file_path.open() as file:
        for line in file:
            report: list[int] = list(map(int, line.split()))
            list_of_reports.append(report)
    return list_of_reports

def safety_test_1(deltas: list[int]) -> int:
    return abs(sum(x > 0 for x in deltas) - sum(x < 0 for x in deltas))

def safety_test_2(deltas: list[int]) -> int:
    delta_limit = 4
    deltas_above_limit: list[int] = [abs(num) >= delta_limit for num in deltas]
    return sum(deltas_above_limit)

def is_safe(report: list[int]) -> bool:
    deltas: list[int] = [b-a for a,b in itertools.pairwise(report)]
    pass_test_1: bool = safety_test_1(deltas) >= len(deltas)
    pass_test_2: bool = safety_test_2(deltas) == 0
    return pass_test_1 and pass_test_2

def day_2_part_1(reports: list[list[int]]) -> int:
    safe_reports: list[bool] = []
    for report in reports:
        safety: bool = is_safe(report)
        safe_reports.append(safety)
    return sum(safe_reports)

def day_2_part_2(reports: list[list[int]]) -> int:
    safe_reports: list[bool] = []
    for report in reports:
        if is_safe(report):
            safe_reports.append(True)
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safe_reports.append(True)
                    break
            else:
                safe_reports.append(False)
    return sum(safe_reports)

file_path: Path = Path.cwd() / "Input" / "day2.txt"
reports: list[list[int]] = read_input(file_path)
print(day_2_part_1(reports))
print(day_2_part_2(reports))