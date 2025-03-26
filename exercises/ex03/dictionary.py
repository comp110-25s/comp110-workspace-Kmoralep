"""These are dictionaries with different purposes!"""

__author__: str = "730765838"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """This function will inverse the keys and values of the original dict."""
    new_dict = {}
    for key in old_dict:
        new_value = key
        new_key = old_dict[key]
        if new_key in new_dict:
            raise KeyError("There can not be duplicates of keys, only values!!!")
        new_dict[new_key] = new_value
    return new_dict


def count(num: list[str]) -> dict[str, int]:
    """This function will give a dict with words and its count of repeated times."""
    results = {}
    for key in num:
        results_key = key
        if results_key in results:
            results[key] += 1
        else:
            results[key] = 1
    return results


def favorite_color(the_colors: dict[str, str]) -> str:
    """This function will tell the fav color from a dict of names and colors."""
    color: str = ""
    list_color: list[str] = []
    counting: int = 0

    for key in the_colors:
        new_key = the_colors[key]
        list_color.append(new_key)
    new_dict = count(list_color)
    for key in new_dict:
        if new_dict[key] > counting:
            counting = new_dict[key]
            color = key
    return color


def bin_len(the_list: list[str]) -> dict[int, set[str]]:
    """This function will turn a list into a dict based on the word length."""
    the_dict: dict[int, set[str]] = {}
    for key in the_list:
        if len(key) in the_dict:
            the_dict[len(key)].add(key)
        else:
            the_dict[len(key)] = set()
            the_dict[len(key)].add(key)
    return the_dict
