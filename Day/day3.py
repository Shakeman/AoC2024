import re
from pathlib import Path
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from collections.abc import Iterator


def find_and_multiply(input_string: str) -> int:
    # Define the regex pattern to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches in the input string
    matches: list[tuple[str, str]] = re.findall(pattern, input_string)

    # Initialize the sum of results
    total_sum = 0

    # Iterate over the matches and perform the multiplications
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y

    return total_sum


def find_and_multiply_and_do(input_string: str) -> int:
    # Define the regex patterns to match valid instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Find all matches in the input string
    mul_matches: Iterator[re.Match[str]] = re.finditer(mul_pattern, input_string)
    do_matches: Iterator[re.Match[str]] = re.finditer(do_pattern, input_string)
    dont_matches: Iterator[re.Match[str]] = re.finditer(dont_pattern, input_string)

    # Initialize the sum of results and the enabled flag
    total_sum = 0
    enabled = True

    # Create a list of all instructions with their positions
    instructions: list[tuple[int, Literal["mul"], tuple[str, str]] | tuple[int, str]] = (
        [(match.start(), "do") for match in do_matches]
        + [(match.start(), "don't") for match in dont_matches]
        + [(match.start(), "mul", match.groups()) for match in mul_matches]
    )  # type: ignore[AssignmentType]

    # Sort instructions by their positions
    instructions.sort()

    # Iterate over the instructions and perform the operations
    for instruction in instructions:
        if instruction[1] == "do":
            enabled = True
        elif instruction[1] == "don't":
            enabled = False
        elif instruction[1] == "mul" and enabled:
            x, y = map(int, instruction[2])  # type: ignore[GeneralTypeIssues]
            total_sum += x * y

    return total_sum


file_path: Path = Path.cwd() / "Input" / "day3.txt"
corrupted_memory: str = file_path.read_text()
result_1: int = find_and_multiply(corrupted_memory)
result_2: int = find_and_multiply_and_do(corrupted_memory)
print(result_1)
print(result_2)
