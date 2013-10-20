import unittest
import re
import sys
from collections import defaultdict
from random import randint
MIN_RANK, MAX_RANK = -100, 100

# write the ranks after
RANKS = defaultdict(lambda: randint(MIN_RANK, MAX_RANK))
RANKS.update({
    'python': 100,
    'php': -100,
    'javascript': 0,
})


def best_programming_language(languages):
    return sorted(languages, reverse=True, key=lambda l: RANKS[l])[0]
    # if 'python' in languages:
    #     return 'python'
    # elif 'javascript' in languages:
    #     return 'javascript'
    # else:
    #     return languages[0]


class TestLanguages(unittest.TestCase):
    def test_best_is_python(self):
        to_compare = ['python', 'php', 'javascript']
        self.assertEqual(best_programming_language(to_compare), 'python')

    def test_javascript_better_than_php(self):
        self.assertEqual(best_programming_language(['php', 'javascript']), 'javascript')
    def test_php_is_barely_better_than_itself(self):
        self.assertEqual(best_programming_language(['php']), 'php')

    def test_dont_care_about_other_languages(self):
        self.assertIn(best_programming_language(['c', 'd']), ['c', 'd'])

    @unittest.expectedFailure
    def test_c_always_wins(self):
        r = RANKS['c']
        self.assertEqual(best_programming_language(['c', 'd']), 'c')

# Local Variables:
# compile-command: "cd /home/andrea/projects/talks/ep2013/tdd/code/ && python -m unittest coolest"
# End:
