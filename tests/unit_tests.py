#!/bin/python3

import unittest
from sys import path, stdout, stderr
from os import system, dup, dup2, pipe, read, WEXITSTATUS
from contextlib import contextmanager
import random
import unittest.mock as mock

path.insert(0, "src/")

from Decision import Decision
from PrisonersPenalties import PrisonersPenalties
from PointsAttributor import PointsAttributor
from PrisonerDecisionsHistory import PrisonerDecisionsHistory
from ImitationStrategy import ImitationStrategy
from HistoryStrategy import HistoryStrategy

class RedirectStream:
    def __init__(self) -> None:
        self.ifd, self.ofd = pipe()

    @contextmanager
    def redirect_stream(self, stream):
        old_stdout = dup(stream.fileno())
        try:
            dup2(self.ofd, stream.fileno())
            yield
        finally:
            dup2(old_stdout, stream.fileno())
    
    def getvalue(self, size) -> str:
        return read(self.ifd, size).decode()

class TestExemple(unittest.TestCase):

    def testIfTwoAreSilent(self):
        expected = PrisonersPenalties(-1, -1)
        prisonerOneDecision = Decision.IsSilent
        prisonerTwoDecision = Decision.IsSilent
        attributor = PointsAttributor()
        got = attributor.getPoints(prisonerOneDecision, prisonerTwoDecision)
        self.assertEqual(expected, got)

    def testIfOneIsSilentAndTwoDenounces(self):
        expected = PrisonersPenalties(-10, 0)
        prisonerOneDecision = Decision.IsSilent
        prisonerTwoDecision = Decision.Denounces
        attributor = PointsAttributor()
        got = attributor.getPoints(prisonerOneDecision, prisonerTwoDecision)
        self.assertEqual(expected, got)

    def testIfOneDenouncesAndTwoIsSilent(self):
        expected = PrisonersPenalties(0, -10)
        prisonerOneDecision = Decision.Denounces
        prisonerTwoDecision = Decision.IsSilent
        attributor = PointsAttributor()
        got = attributor.getPoints(prisonerOneDecision, prisonerTwoDecision)
        self.assertEqual(expected, got)

    def testIfTwoDenounce(self):
        expected = PrisonersPenalties(-5, -5)
        prisonerOneDecision = Decision.Denounces
        prisonerTwoDecision = Decision.Denounces
        attributor = PointsAttributor()
        got = attributor.getPoints(prisonerOneDecision, prisonerTwoDecision)
        self.assertEqual(expected, got)

    @mock.patch('random.choice')
    def testImitationStrategy(self, random_mock):
        random_mock.return_value = 1
        expected = Decision.Denounces
        peerDecisionsHistory = PrisonerDecisionsHistory
        strategy = ImitationStrategy(peerDecisionsHistory)
        # with mock.patch('random.random', myRandom):
        got = strategy.getDecision(1)
        self.assertEqual(expected, got)
        
    def test_binary(self):
        out = RedirectStream()
        binary = "/usr/bin/echo"
        argv = [binary, "Hello World"]
        command = " ".join(argv)
        expected_exit_code = 0
        ifs = open("tests/results/echoresult")
        expected = ifs.read()

        ifs.close()
        with out.redirect_stream(stdout):
            status = system(command)
            exit_code = WEXITSTATUS(status)
            got = out.getvalue(len(expected))
            self.assertEqual(expected, got)
            self.assertEqual(expected_exit_code, exit_code)

    def test_binary_bad_arguments(self):
        out = RedirectStream()
        binary = "/usr/bin/ls"
        argv = [binary, "non_existent_file"]
        command = " ".join(argv)
        expected_exit_code = 2

        with out.redirect_stream(stderr):
            status = system(command)
            exit_code = WEXITSTATUS(status)
            self.assertEqual(expected_exit_code, exit_code)

if __name__ == '__main__':
    unittest.main()
