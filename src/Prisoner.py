##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## Prisoner
##

from Decision import Decision
from PrisonerStrategy import PrisonerStrategy

class Prisoner:
    def __init__(self, strategy: PrisonerStrategy) -> None:
        self.strategy = strategy

    def getDecision(self, round: int) -> Decision:
        return self.strategy.getDecision(round)
