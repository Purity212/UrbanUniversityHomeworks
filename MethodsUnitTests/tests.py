from runner_and_tournament import Runner, Tournament
import unittest
from pprint import pprint


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r_1 = Runner('Усейн', 10)
        self.r_2 = Runner('Андрей', 9)
        self.r_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t = Tournament(90, self.r_1, self.r_3)
        self.all_results = t.start()
        print(self.all_results)
        self.assertTrue(list(self.all_results.keys())[-1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t = Tournament(90, self.r_2, self.r_3)
        self.all_results = t.start()
        print(self.all_results)
        self.assertTrue(list(self.all_results.keys())[-1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t = Tournament(90, self.r_1, self.r_2, self.r_3)
        self.all_results = t.start()
        print(self.all_results)
        self.assertTrue(list(self.all_results.keys())[-1], 'Ник')


if __name__ == '__main__':
    unittest.main()
