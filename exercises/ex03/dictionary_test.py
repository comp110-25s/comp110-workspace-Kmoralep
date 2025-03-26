"""This is the testing area for my dictionaries."""

__author__: str = "730765838"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len
import pytest

# Create 3 tests for each function below. One edge and two uses cases.


def test_invert_use() -> None:
    assert invert({"3": "Three"}) == ({"Three": "3"})


def test_invert_use2() -> None:
    assert invert({"up": "down", "left": "right", "east": "west"}) == (
        {"down": "up", "right": "left", "west": "east"}
    )


def test_invert_edge() -> None:
    assert invert({"": "2"}) == ({"2": ""})


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_count_use() -> None:
    assert count(["cat", "dog", "cat", "bird", "rabbit"]) == (
        {"cat": 2, "dog": 1, "bird": 1, "rabbit": 1}
    )


def test_count_use2() -> None:
    assert count(["NC", "SC", "NC", "NY", "SC", "CA"]) == (
        {"NC": 2, "SC": 2, "NY": 1, "CA": 1}
    )


def test_count_edge() -> None:
    assert count(["3", "4", "5", "6"]) == ({"3": 1, "4": 1, "5": 1, "6": 1})


def test_favorite_color_use() -> None:
    assert favorite_color({"Kim": "Blue", "Kat": "Pink", "Jas": "Blue"}) == "Blue"


def test_favorite_color_use2() -> None:
    assert (
        favorite_color(
            {"Taylor": "Teal", "Tris": "Teal", "Ken": "Green", "Barb": "Green"}
        )
        == "Teal"
    )


def test_favorite_color_edge() -> None:
    assert (
        favorite_color(
            {"Sam": "Orange", "Bella": "Purple", "Ash": "purple", "Hector": "Orange"}
        )
        == "Orange"
    )


def test_bin_lin_use() -> None:
    assert bin_len(["sam", "loves", "her", "cat"]) == {
        3: {"sam", "her", "cat"},
        5: {"loves"},
    }


def test_bin_lin_use2() -> None:
    assert bin_len(["north", "south", "east", "west"]) == {
        5: {"north", "south"},
        4: {"east", "west"},
    }


def test_bin_lin_edge() -> None:
    assert bin_len([]) == {}
