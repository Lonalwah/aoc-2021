from pathlib import Path
import sys


def parse(filePath: str) -> list[int]:
    inputs = Path(filePath).read_text().strip()
    return list(map(int, inputs.split("\n")))


def part1(inputs: list[int]) -> int:
    count = 0
    for i in range(0, len(inputs)):
        if inputs[i] > inputs[i - 1]:
            count += 1
    return count


def solve(filePath: str):
    p1 = part1(parse(filePath))
    print(f"Day 1 - Part 1 Solution: {p1}")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        solve(path)
