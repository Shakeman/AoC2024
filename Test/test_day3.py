from Day.day3 import find_and_multiply


def test_day3_part1() -> None:
    example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert find_and_multiply(example) == 161