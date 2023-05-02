##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## PrisonerPointsHistory
##

from PrisonersPenalties import PrisonersPenalties

class PrisonersPenaltiesHistory:
    def __init__(self) -> None:
        self.pointsHistory = []

    def getAllPenalties(self) -> list[PrisonersPenalties]:
        return self.pointsHistory
    
    def getRoundPenalties(self, round: int) -> PrisonersPenalties:
        return self.pointsHistory[round]

    def insertRoundPenalties(self, penalties: PrisonersPenalties) -> None:
        self.pointsHistory.append(penalties)
