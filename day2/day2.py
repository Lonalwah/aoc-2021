import sys
from pathlib import Path


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __str__(self):
        return f"x:{self.x} y:{self.y}"


# Read command
def parse(filePath: str) -> list[int]:
    inputs = Path(filePath).read_text().strip()
    return inputs.split("\n")


def ReadCommand(cmdIn: str) -> Vector2:
    # tokenise where 0 is direction and 1 is distance
    cmd = cmdIn.split(" ")

    if len(cmd) >= 2 and cmd[0] != "" and cmd[1].isnumeric():
        mag = int(cmd[1])
        if cmd[0] == "forward":
            return Vector2(x=mag)
        elif cmd[0] == "up":
            return Vector2(y=-mag)
        elif cmd[0] == "down":
            return Vector2(y=mag)
    pass


def Part1(inputs: list[str]) -> int:
    subPos = Vector2()
    for i in inputs:
        subPos += ReadCommand(i)
    return subPos.x * subPos.y


def solve(path: str) -> int:
    print(f"Day 2 - Part 1 Solution: {Part1(parse(path))}")
    return 0


if __name__ == "__main__":
    for path in sys.argv[1:]:
        solve(path)
