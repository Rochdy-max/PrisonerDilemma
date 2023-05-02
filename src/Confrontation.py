##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## Confrontation
##

from Prisoner import Prisoner
from Decision import Decision
from PrisonerDecisionsHistory import PrisonerDecisionsHistory
from PointsAttributor import PointsAttributor
from PrisonersPenalties import PrisonersPenalties

class Confrontation:
    def __init__(self, prisonerOne: Prisoner, prisonerTwo: Prisoner, prisonerOneDecisions: PrisonerDecisionsHistory, prisonerTwoDecisions: PrisonerDecisionsHistory) -> None:
        self.prisonerOne = prisonerOne
        self.prisonerTwo = prisonerTwo
        self.prisonerOneDecisions = prisonerOneDecisions
        self.prisonerTwoDecisions = prisonerTwoDecisions
        self.attributor = PointsAttributor()

    def play(self, round: int) -> PrisonersPenalties:
        decisionOne = self.prisonerOne.getDecision(round)
        decisionTwo = self.prisonerTwo.getDecision(round)
        if round > 1:
            print()
            print("*" * 30)
            print()
        print("Round %d:\n" % round)
        print("Prisoner 1 decides to", "denounce" if decisionOne == Decision.Denounces else "be silent")
        print("Prisoner 2 decides to", "denounce" if decisionTwo == Decision.Denounces else "be silent")
        self.prisonerOneDecisions.insertRoundDecision(decisionOne)
        self.prisonerTwoDecisions.insertRoundDecision(decisionTwo)
        prisonerPoints = self.attributor.getPoints(decisionOne, decisionTwo)
        return prisonerPoints
