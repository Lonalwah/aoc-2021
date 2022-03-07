from pathlib import Path
import day3

PROJECT_DIR: str = Path(__file__).parent


def test_GetMostCommon():
    assert day3.GetMostCommon(["1", "0", "1", "0", "1"]) == "1"
    assert day3.GetMostCommon(["1", "0", "1", "0", "0"]) == "0"


def test_GetLeastCommon():
    assert day3.GetLeastCommon(["1", "0", "1", "0", "1"]) == "0"
    assert day3.GetLeastCommon(["1", "0", "1", "0", "0"]) == "1"


def test_GetElipsonRate():
    input = day3.Parse(f"{PROJECT_DIR}/example.txt")
    assert day3.GetElipsonRate(input) == 9


def test_GetGammaRate():
    input = day3.Parse(f"{PROJECT_DIR}/example.txt")
    assert day3.GetGammaRate(input) == 22
