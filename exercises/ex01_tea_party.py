"""Calculate how many tea bags and treats we will need for a party."""

__author__: str = "730765838"


def main_planner(guests: int) -> None:
    """Helps us plan altogether the cost and items."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate how many tea bags per person."""
    return people * 2


def treats(people: int) -> int:
    """Calculate how many treats per person."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """How much will these items cost us?"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
