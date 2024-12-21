import unittest
import tests_12_3


run_walkST = unittest.TestSuite()
run_walkST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunerTest))
run_walkST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

STrunner = unittest.TextTestRunner(verbosity=2)
STrunner.run(run_walkST)