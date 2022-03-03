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


def part2(inputs: list[int]) -> int:
    # 3 sliding window
    x = []
    for i in range(0, len(inputs) - 2):
        x.append(inputs[i] + inputs[i + 1] + inputs[i + 2])

    # Run part1 from map 3 sliding window
    return part1(x)


def solve(filePath: str):
    p1 = part1(parse(filePath))
    print(f"Day 1 - Part 1 Solution: {p1}")

    p2 = part2(parse(filePath))
    print(f"Day 1 - Part 2 Solution: {p2}")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        solve(path)
