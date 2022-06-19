import math
import re


class Board:
    def __init__(self, input) -> None:
        self.ParseBoard(input)
        self.marked = []
        pass

    def ParseBoard(self, input: str):
        lines = input.split("\n")
        self.col = len(lines)
        self.row = len(re.findall(r"\d+", lines[0]))
        self.board = [int(i) for i in re.findall(r"\d+", input)]
        pass

    def get_col(self, index: int) -> int:
        return math.floor(index % self.col)

    def get_row(self, index: int) -> int:
        return math.floor(index / self.col)

    def check_win_condition(self) -> bool:
        for r in range(0, self.row):
            rows = [q for q in self.marked if q["row"] == r]
            if len(rows) >= 5:
                return True

        for c in range(0, self.col):
            cols = [q for q in self.marked if q["col"] == c]
            if len(cols) >= 5:
                return True
        return False

    def mark(self, number: int):
        try:
            index = self.board.index(number)
            r = self.get_row(index)
            c = self.get_col(index)
            self.marked.append({"row": r, "col": c})
        except ValueError:
            pass

    def __repr__(self) -> str:
        result = ""
        for r in range(self.row):
            offset = r * self.row
            lbound = 0 + offset
            hbound = self.col + offset
            result += "\n" + ", ".join(self.board[lbound:hbound])
        return result + "\n"


class Boards:
    def __init__(self) -> None:
        self.winningBoard = None
        self.boards = []

    def AddBoard(self, input) -> None:
        self.boards.append(Board(input))

    def Mark(self, number: int) -> None:
        for i in range(0, len(self.boards)):
            self.boards[i].mark(number)

    def CheckWinner(self) -> bool:
        for ind, board in enumerate(self.boards):
            if board.check_win_condition():
                self.winningBoard = board
                return True
        return False
