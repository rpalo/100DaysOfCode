"""Checks the scrabble word-scores of words"""

from collections import defaultdict

from data import LETTER_SCORES

FORGIVING_SCORES = defaultdict(int)
FORGIVING_SCORES.update(LETTER_SCORES)


def load_words(filename):
    """Loads a dictionary file into a list of words"""
    with open(filename, "r") as f:
        return [word for word in f.read().split("\n") if word]


def scrabble_score(word):
    """Scores a word using American scrabble scores.
    word: a string to be scored
    returns: an integer score
    """
    return sum(FORGIVING_SCORES[letter] for letter in word.upper())


def best_scrabble_word(words):
    """Returns the best word and its score from a list of words.
    words: list of strings
    returns: tuple (best word, score)
    """
    scored_words = [(word, scrabble_score(word)) for word in words]
    return max(scored_words, key=lambda x: x[1])


if __name__ == "__main__":
    # Find best word in dictionary
    words = load_words("dictionary.txt")
    best_word, score = best_scrabble_word(words)
    print(f"Best word: {best_word} - {score} points.")
    exit(0)
