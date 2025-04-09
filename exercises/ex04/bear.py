"""File to define Bear class."""

__author__: str = "730765838"


class Bear:
    age: int
    hunger_score: int

    def __init__(self) -> None:
        """The start of the bear cycle."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Bears will age by 1 and hunger will decrease by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Bears hunger is equal to amount of fish."""
        self.hunger_score = num_fish
