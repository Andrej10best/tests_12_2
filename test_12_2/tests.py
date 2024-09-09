import unittest
from unittest import TestCase
from main import Runner, Tournament


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            dict_ = {}
            for key, val in result.items():
                dict_[key] = val.name
            print(dict_)

    def test_start_runner_1(self):
        self.race = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.race.start()
        result_win = self.all_results[max(self.all_results.keys())]
        self.assertTrue(result_win == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_start_runner_2(self):
        self.race = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.race.start()
        result_win = self.all_results[max(self.all_results.keys())]
        self.assertTrue(result_win == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_start_runner_3(self):
        self.race = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = self.race.start()
        result_win = self.all_results[max(self.all_results.keys())]
        self.assertTrue(result_win == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
