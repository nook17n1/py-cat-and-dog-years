import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (-27, -27, [0, 0]),
        (100, 100, [21, 17]),
    ],)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_error_if_name_not_exist() -> None:
    with pytest.raises(KeyError):
        get_human_age(None, 21)


def test_should_raise_error_if_name_is_str() -> None:
    with pytest.raises(AttributeError):
        get_human_age(21, "21")
