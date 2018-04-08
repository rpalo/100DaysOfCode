import unittest

from word_score import load_words, scrabble_score, best_scrabble_word

TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')


class TestWordValue(unittest.TestCase):

    def test_load_words(self):
        words = load_words("dictionary.txt")
        self.assertEqual(len(words), 235886)
        self.assertEqual(words[0], 'A')
        self.assertEqual(words[-1], 'Zyzzogeton')
        self.assertNotIn(' ', ''.join(words))

    def test_scrabble_score(self):
        self.assertEqual(scrabble_score('bob'), 7)
        self.assertEqual(scrabble_score('JuliaN'), 13)
        self.assertEqual(scrabble_score('PyBites'), 14)
        self.assertEqual(scrabble_score('benzalphenylhydrazone'), 56)

    def test_best_scrabble_word(self):
        dictionary_words = load_words("dictionary.txt")
        self.assertEqual(best_scrabble_word(TEST_WORDS)[0], 'barbeque')
        self.assertEqual(best_scrabble_word(dictionary_words)[0],
                         'benzalphenylhydrazone')


if __name__ == "__main__":
    unittest.main()
