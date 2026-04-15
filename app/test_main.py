from app.main import get_human_age


def test_for_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_for_all_less_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_for_all_less_24_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_for_all_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_for_all_less_25_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_for_all_less_30_years() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_for_negetive_years() -> None:
    assert get_human_age(-15, -15) == [0, 0]


def test_for_different_years() -> None:
    assert get_human_age(24, 18) == [2, 1]


def test_for_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
