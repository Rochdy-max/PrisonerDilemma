##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## HistoryStrategy
##

from Decision import Decision
from PrisonerDecisionsHistory import PrisonerDecisionsHistory
from PrisonerStrategy import PrisonerStrategy
from random import choice, seed
from time import time

class HistoryStrategy(PrisonerStrategy):
    def __init__(self, peerDecisionsHistory: PrisonerDecisionsHistory) -> None:
        super().__init__(peerDecisionsHistory)

    @staticmethod
    def getMajoritaryDecision(peerDecisionsHistory: PrisonerDecisionsHistory) -> Decision:
        peerDecisions = peerDecisionsHistory.getAllDecisions()
        nbDenonciations = peerDecisions.count(Decision.Denounces)
        nbSilences = peerDecisions.count(Decision.IsSilent)
        if nbDenonciations > nbSilences:
            return Decision.Denounces
        else:
            return Decision.IsSilent

    def getDecision(self, round: int) -> Decision:
        if round == 1:
            return Decision.IsSilent
        if round == 2:
            seed(time())
            nbDecisions = len(Decision)
            decision = choice(range(nbDecisions))
            return Decision(decision)
        return self.getMajoritaryDecision(self.peerDecisionsHistory)
