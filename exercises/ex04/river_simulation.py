"""This is a simulation of a river ecosystem."""

__author__: str = "730765838"

from exercises.ex04.river import River

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()
my_river.one_river_day()
