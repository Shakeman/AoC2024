from pathlib import Path

def read_input(file_path: Path) -> tuple[list[int], list[int]]:
    left_list: list[int] = []
    right_list: list[int] = []
    with file_path.open() as file:
        for line in file:
            left: int
            right: int
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def day_1_part_1(left_list: list[int], right_list: list[int]) -> int:
    sorted_left_list: list[int] = sorted(left_list)
    sorted_right_list: list[int] = sorted(right_list)
    differences: list[int] = calculate_differences(sorted_left_list, sorted_right_list)
    return sum(differences)

def day_1_part_2(left_list: list[int], right_list: list[int]) -> int:
    sorted_left_list: list[int] = sorted(left_list)
    sorted_right_list: list[int] = sorted(right_list)
    counts: list[int] = count_occurrences(sorted_left_list, sorted_right_list)
    similarity: list[int] = multiply_lists(counts, sorted_left_list)
    return sum(similarity)

def calculate_differences(list1: list[int], list2: list[int]) -> list[int]:
    return [abs(a - b) for a, b in zip(list1, list2)]

def count_occurrences(left_list: list[int], right_list: list[int]) -> list[int]:
    return [right_list.count(item) for item in left_list]

def multiply_lists(list1: list[int], list2: list[int]) -> list[int]:
    return [a * b for a, b in zip(list1, list2)]

file_path: Path = Path.cwd() / "Input" / "day1.txt"
left_list, right_list = read_input(file_path)
print(day_1_part_1(left_list, right_list))
print(day_1_part_2(left_list, right_list))
