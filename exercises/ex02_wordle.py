"""This is a wordle game!"""

__author__ = "730765838"


def contains_char(word: str, letter: str) -> bool:
    """This will check the length of the word and verify the letter."""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0
    while idx < len(word):  # Loops as long as index is less than length of word.
        if word[idx] == letter:
            return True
        else:
            idx = (
                idx + 1
            )  # Base Case: Makes sure that we get a stopping point for the loop.
    return False


def emojified(guess: str, secret_word: str) -> str:
    """This function use emojis to tell user if they are correctly guessing."""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    emojis_together = ""  # Empty string that will combine emojis later in one line.
    while idx < len(guess):  # Loops as long as index is less than guess word.
        if guess[idx] == secret_word[idx]:
            emojis_together = emojis_together + GREEN_BOX
        elif contains_char(
            word=secret_word, letter=guess[idx]
        ):  # Uses contains char fucntion to determine if letter is valid.
            emojis_together = emojis_together + YELLOW_BOX
        else:
            emojis_together = emojis_together + WHITE_BOX
        idx = (
            idx + 1
        )  # Base Case: Makes sure that we get a stopping point for the loop.
    return emojis_together


def input_guess(word_length: int) -> str:
    user = input(f"Enter a {word_length} character word: ")
    if len(user) == word_length:
        return user
    try_again: str = ""  # Returns input if it is the correct length
    while len(try_again) != word_length:
        try_again = input(f"That wasn't {word_length} chars! Try again:")
        if len(try_again) == word_length:
            return try_again
    return try_again
    # This is another way to check if input is not equal to length of word.
    # while len(user) != word_length:
    #     user = input(f"That wasn't {word_length} chars! Try again:")
    #     if len(user) == word_length:
    #         return user
    # return user


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    n: int = 1
    win: bool = False  # Variable used to help determine if user has won or not.

    while n <= 6 and win is False:
        print(f"=== Turn {n}/6 ===")
        guess: str = input_guess(
            word_length=len(secret)
        )  # Uses input_guess as a variable
        print(
            emojified(guess=guess, secret_word=secret)
        )  # Uses emojified function to print emojis for user inut from guess variable.
        if secret == guess:
            print(f"You won in {n}/6 turns!")
            win = True  # Win value cahnges to true if game is won.
        else:
            n = n + 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")  # Hardcodes secret word as codes for the user playing.
