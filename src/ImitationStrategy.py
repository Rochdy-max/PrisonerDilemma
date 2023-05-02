##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## ImitationStrategie
##

from Decision import Decision
from PrisonerDecisionsHistory import PrisonerDecisionsHistory
from PrisonerStrategy import PrisonerStrategy
from random import choice, seed
from time import time

class ImitationStrategy(PrisonerStrategy):
    def __init__(self, peerDecisionsHistory: PrisonerDecisionsHistory) -> None:
        super().__init__(peerDecisionsHistory)

    def getDecision(self, round: int) -> Decision:
        if round == 1 or round == 2:
            seed(time())
            nbDecisions = len(Decision)
            decision = choice(range(nbDecisions))
            # print("decision is", decision)
            return Decision(decision)
        peerDecisions = self.peerDecisionsHistory.getAllDecisions()
        return peerDecisions[-1]
