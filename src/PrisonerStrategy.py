##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## PrisonerStrategy
##

from Decision import Decision
from PrisonerDecisionsHistory import PrisonerDecisionsHistory

class PrisonerStrategy:
    def __init__(self, peerDecisionsHistory: PrisonerDecisionsHistory) -> None:
        self.peerDecisionsHistory = peerDecisionsHistory

    def getDecision(self, round: int) -> Decision:
        pass
