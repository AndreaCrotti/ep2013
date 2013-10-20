import unittest

LANGUAGES = ['php', 'javascript', 'python']

class Ranking(dict):
    """Dictionary supporting lower/upper case access
    """
    def __getitem__(self, item):
        return super(Ranking, self).__getitem__(item.lower())


RANKING = Ranking({
    'python': 100,
    'javascript': 0,
    'php': -100,
})


def best_programming_language(languages):
    def by_ranking(language):
        if language in RANKING:
            return RANKING[language]
        else:
            return -1000

    lower_languages = map(lambda w: w.lower(), languages)
    return sorted(lower_languages, key=by_ranking)[-1]


class TestLanguages(unittest.TestCase):
    def test_best_programming_language_is_python(self):
        self.assertEqual(best_programming_language(LANGUAGES), 'python')

    def test_javascript_better_than_php(self):
        self.assertEqual(best_programming_language(['php', 'javascript']), 'javascript')

    def test_passing_uppercase_string_works(self):
        self.assertEqual(best_programming_language(['Php', 'Python', 'javascript']), 'python')

    def test_unknown_language_is_bad_by_definition(self):
        self.assertEqual(best_programming_language(['python', 'brainkfuck']), 'python')

# Local Variables:
# compile-command: "cd /home/andrea/projects/talks/ep2013/tdd/code/ && python -m unittest coolest_train"
# End:
