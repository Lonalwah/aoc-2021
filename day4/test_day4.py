from pathlib import Path
from board import Board
import day4

PROJECT_DIR: str = Path(__file__).parent


def test_board():
    test_input = """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19"""

    board = Board(test_input)

    assert board.get_col(0) == 0
    assert board.get_col(6) == 1
    assert board.get_col(10) == 0

    assert board.get_row(0) == 0
    assert board.get_row(6) == 1
    assert board.get_row(10) == 2

    test_draw = [21, 9, 14, 16, 7]

    for draw in test_draw:
        assert board.check_win_condition() is False
        board.mark(draw)

    assert board.check_win_condition() is True


def test_Part1():
    input_path = f"{PROJECT_DIR}/example.txt"
    assert day4.Part1(input_path) == 4512
