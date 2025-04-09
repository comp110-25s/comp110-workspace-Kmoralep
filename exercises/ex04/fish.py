"""File to define Fish class."""

__author__: str = "730765838."


class Fish:
    age: int

    def __init__(self) -> None:
        """The start of the fish cycle."""
        self.age = 0

    def one_day(self) -> None:
        """Fishes will age by 1."""
        self.age += 1
