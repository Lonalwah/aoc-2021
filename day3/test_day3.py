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


def test_PowerConsumption():
    input = day3.Parse(f"{PROJECT_DIR}/example.txt")
    powerConsumption = day3.GetGammaRate(input) * day3.GetElipsonRate(input)
    assert powerConsumption == 198


def test_GetOxyRating():
    input = day3.Parse(f"{PROJECT_DIR}/example.txt")
    assert day3.GetOxyRating(input) == 23


def test_GetCo2Rating():
    input = day3.Parse(f"{PROJECT_DIR}/example.txt")
    assert day3.GetCo2Rating(input) == 10


def test_LifeSupportRating():
    input = day3.Parse(f"{PROJECT_DIR}/example.txt")
    lifeSupport = day3.GetOxyRating(input) * day3.GetCo2Rating(input)
    assert lifeSupport == 230
