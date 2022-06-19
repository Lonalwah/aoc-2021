import sys
import logging
from pathlib import Path
from board import Boards, Board

logging.basicConfig(encoding="utf-8", level=logging.INFO)


def Parse(filePath: str) -> list[str]:
    try:
        inputs = Path(filePath).read_text().strip()
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    else:
        return inputs.split("\n\n")


def BuildDraws(input: str) -> list[int]:
    draw = [int(i) for i in input.split(",")]
    return draw


def CalculateWinner(b: Board, drawn: list[int]) -> int:
    remaining = [num for num in b.board if num not in drawn]
    return sum(remaining) * drawn[len(drawn) - 1]


def BuildBoards(inputs: list[str]) -> Boards:
    boards = Boards()
    for board in inputs:
        boards.AddBoard(board)
    return boards


def Part1(path: str) -> int:
    input = Parse(path)
    draws = BuildDraws(input[0])
    boards = BuildBoards(input[1:])

    logging.debug(draws)
    for i, d in enumerate(draws):
        logging.debug(f"Draw number: {d}")
        boards.Mark(d)
        if boards.CheckWinner():
            logging.debug(f"Last number draw: {d}")
            logging.debug(f"Drawn numbers: {draws[:i+1]}")
            return CalculateWinner(boards.winningBoard, draws[: i + 1])
    return None


def Solve(path: str):
    # print(f"Day 4 - Part 1 Solution: {Part1(path)}")
    logging.info(Part1(path))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        Solve(path)
