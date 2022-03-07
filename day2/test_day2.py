from pathlib import Path
from day2 import Vector2, ReadCommand, Part1, Part2, Parse

PROJECT_DIR: str = Path(__file__).parent


def test_vector2():
    v1 = Vector2()
    assert v1.x == 0 and v1.y == 0

    v1.x = -10
    assert v1.x == -10

    v2 = Vector2(x=5, y=7)
    assert v2.x == 5 and v2.y == 7

    v = v1 + v2
    assert v.x == -5 and v.y == 7

    v1 += v2
    assert v1.x == -5 and v1.y == 7


def test_read_command():
    v = ReadCommand("forward 10")
    assert v.x == 10 and v.y == 0

    v = ReadCommand("up 7")
    assert v.x == 0 and v.y == -7

    v = ReadCommand("down 10")
    assert v.x == 0 and v.y == 10

    v = ReadCommand("ahdfkdsan")
    assert v is None

    v = ReadCommand("ahdf kdsan")
    assert v is None


def test_day2_part1_example():
    p = Parse(f"{PROJECT_DIR}/example.txt")
    assert Part1(p) == 150


def test_day2_part2_example():
    p = Parse(f"{PROJECT_DIR}/example.txt")
    assert Part2(p) == 900
