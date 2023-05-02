##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## PrisonerDilemma
##

from PrisonerDecisionsHistory import PrisonerDecisionsHistory
from ImitationStrategy import ImitationStrategy
from HistoryStrategy import HistoryStrategy
from Prisoner import Prisoner
from Confrontation import Confrontation
from PrisonersPenaltiesHistory import PrisonersPenaltiesHistory

class PrisonerDilemmaGame:
    def __init__(self) -> None:
        self.prisonerOneDecisions = PrisonerDecisionsHistory()
        self.prisonerTwoDecisions = PrisonerDecisionsHistory()
        self.prisonerOneStrategy = ImitationStrategy(self.prisonerTwoDecisions)
        self.prisonerTwoStrategy = HistoryStrategy(self.prisonerOneDecisions)
        self.prisonerOne = Prisoner(self.prisonerOneStrategy)
        self.prisonerTwo = Prisoner(self.prisonerTwoStrategy)
        self.penaltiesHistory = PrisonersPenaltiesHistory()

    def play(self, nbRounds: int = 6) -> None:
        confrontation = Confrontation(self.prisonerOne, self.prisonerTwo, self.prisonerOneDecisions, self.prisonerTwoDecisions)
        for round in range(1, nbRounds + 1):
            penalties = confrontation.play(round)
            self.penaltiesHistory.insertRoundPenalties(penalties)

    def reviewParty(self):
        prisonerOnePoints = 0
        prisonerTwoPoints = 0
        for penalties in self.penaltiesHistory.getAllPenalties():
            prisonerOnePoints += penalties.prisonerOnePenalty
            prisonerTwoPoints += penalties.prisonerTwoPenalty
        print()
        print("*" * 30)
        print()
        if prisonerOnePoints > prisonerTwoPoints:
            print("Prisoner 1 won with %d points against Prisoner 2 with %d points"
                  % (prisonerOnePoints, prisonerTwoPoints))
        if prisonerOnePoints < prisonerTwoPoints:
            print("Prisoner 2 won with %d points against Prisoner 1 with %d points"
                  % (prisonerTwoPoints, prisonerOnePoints))
        if prisonerOnePoints == prisonerTwoPoints:
            print("This is an equality of %d points" % prisonerOnePoints)