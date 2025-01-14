from HumanMoveTest.tests import RunnerTests
from MethodsUnitTests.tests import TournamentTest
import unittest

runnerTournamentST = unittest.TestSuite()

runnerTournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTests))
runnerTournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    test_runner.run(runnerTournamentST)

