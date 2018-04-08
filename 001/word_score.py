"""Checks the scrabble word-scores of words"""

from collections import defaultdict

from data import LETTER_SCORES

FORGIVING_SCORES = defaultdict(int)
FORGIVING_SCORES.update(LETTER_SCORES)


def scrabble_score(word):
    """Scores a word using American scrabble scores.
    word: a string to be scored
    returns: an integer score
    """
    return sum(FORGIVING_SCORES[letter] for letter in word.upper())


if __name__ == "__main__":
    # Find best word in dictionary
    with open("dictionary.txt", "r") as f:
        words = f.read().split("\n")

    best_word = max(words, key=scrabble_score)
    print(f"Best word: {best_word} - {scrabble_score(best_word)} points.")
    exit(0)
