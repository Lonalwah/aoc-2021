import sys
from pathlib import Path


def Parse(filePath: str) -> list[str]:
    inputs = Path(filePath).read_text().strip()
    return inputs.split("\n")


def GetMostCommon(bits: list[str]) -> str:
    return max(set(bits), key=bits.count)


def GetLeastCommon(bits: list[str]) -> str:
    return min(set(bits), key=bits.count)


def GetGammaRate(bits: list[str]) -> int:
    x = [GetMostCommon([b[i] for b in bits]) for i in range(0, len(bits[0]))]
    return int("".join(x), 2)


def GetElipsonRate(bits: list[str]) -> int:
    x = [GetLeastCommon([b[i] for b in bits]) for i in range(0, len(bits[0]))]
    return int("".join(x), 2)


def Part1(inputs: list) -> int:
    return GetGammaRate(inputs) * GetElipsonRate(inputs)


def Solve(path: str):
    print(f"Day 3 - Part 1 Solution: {Part1(Parse(path))}")
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        Solve(path)
