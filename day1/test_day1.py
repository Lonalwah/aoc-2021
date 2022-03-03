from pathlib import Path
import day1

PROJECT_DIR: str = Path(__file__).parent


def test_example_return():
    p = day1.parse(f"{PROJECT_DIR}/example.txt")
    assert all(isinstance(item, int) for item in p)


def test_day1_part1_example():
    p = day1.parse(f"{PROJECT_DIR}/example.txt")
    assert day1.part1(p) == 7


def test_day1_part2_example():
    p = day1.parse(f"{PROJECT_DIR}/example.txt")
    assert day1.part2(p) == 5
