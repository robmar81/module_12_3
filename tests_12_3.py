import runner_and_tournament as rat
import runner
import unittest
import inspect


class RunerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        wlk = runner.Runner('гуляка')
        for i in range(10):
            wlk.walk()
        self.assertEqual(wlk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rnr = runner.Runner('беглец')
        for i in range(10):
            rnr.run()
        self.assertEqual(rnr.distance, 100)


    def test_challenge(self):
        wlk = runner.Runner('гуляка')
        rnr = runner.Runner('беглец')
        for i in range(10):
            wlk.walk()
            rnr.run()
        self.assertNotEqual(wlk.distance, rnr.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.rnr1 = rat.Runner('Усэйн', 10)
        self.rnr2 = rat.Runner('Андрей', 9)
        self.rnr3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({key: str(value) for key, value in cls.all_results[test].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testUsainNik(self):
        tournament = rat.Tournament(90, self.rnr1, self.rnr3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testAndreyNik(self):
        tournament = rat.Tournament(90, self.rnr2, self.rnr3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testUsainAndreyNik(self):
        tournament = rat.Tournament(90, self.rnr1, self.rnr2, self.rnr3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == "__main__":
    unittest.main()
