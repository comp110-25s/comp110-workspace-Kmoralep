"""File to define River class."""

__author__: str = "730765838"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    Bears: list[str]
    Fish: list[str]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """This function will check the age of the bears and fishes."""
        surviving_bears: list[Bear] = self.bears
        surviving_fish: list[Fish] = self.fish
        for fish in self.fish:
            if fish.age < 3:
                surviving_fish.append(fish)
        for bear in self.bears:
            if bear.age < 5:
                surviving_bears.append(bear)

    def remove_fish(self, amount: int) -> None:
        """This function will remove a certain amount of fishes."""
        idx: int = 0
        for idx in range(amount):
            self.fish.pop(idx)
            idx += 1

    def bears_eating(self) -> None:
        """This function will remove eaten fishes."""
        if len(self.fish) == 5:
            self.remove_fish(amount=3)
            for bear in self.bears:
                bear.eat(num_fish=3)

    def check_hunger(self) -> None:
        """This function will check the hunger of bears."""
        surviving_bears: list[Bear] = self.bears
        for bear in self.bears:
            if bear.hunger_score < 0:
                surviving_bears.append(bear)

    def repopulate_fish(self) -> None:
        """This function will add new fishes to the pop."""
        new_fish: list[Fish] = self.fish
        for n in self.fish:
            n = len(self.fish)
            baby_fish = n // 2
            for baby_fish in self.fish:
                new_fish.append(baby_fish)

    def repopulate_bears(self) -> None:
        """This function will add new bears to the pop."""
        new_bears: list[Bear] = self.bears
        for n in self.bears:
            n = len(self.bears)
            baby_bears = n // 2
            for baby_bears in self.bears:
                new_bears.append(baby_bears)

    def view_river(self) -> None:
        """This will check the number of days in the ecosystem & its pop."""
        print(f"~~~ Day: {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        while self.day < 7:
            self.day += 1
            # Simulate one day for all Bears
            for bear in self.bears:
                bear.one_day()
            # Simulate one day for all Fish
            for fish in self.fish:
                fish.one_day()
            # Simulate Bear's eating
            self.bears_eating()
            # Remove hungry Bear's from River
            self.check_hunger()
            # Remove old Fish and Bear's from River
            self.check_ages()
            # Simulate Fish repopulation
            self.repopulate_fish()
            # Simulate Bear repopulation
            self.repopulate_bears()
            # Visualize River
            self.view_river()
