##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## PrisonerDecisionsHistory
##

from Decision import Decision

class PrisonerDecisionsHistory:
    def __init__(self) -> None:
        self.decisions = []

    def getAllDecisions(self) -> list[Decision]:
        return self.decisions

    def getDecisionOfRound(self, round: int) -> Decision:
        return self.decisions[round - 1]

    def insertRoundDecision(self, decision: Decision) -> None:
        self.decisions.append(decision)
