import re
from pathlib import Path


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


file_path: Path = Path.cwd() / "Input" / "day3.txt"
corrupted_memory: str = file_path.read_text()
result: int = find_and_multiply(corrupted_memory)
print(result)  # Output should be 161
