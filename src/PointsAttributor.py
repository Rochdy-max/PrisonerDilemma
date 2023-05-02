##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## PointsAttributor
##

from Decision import Decision
from PrisonersPenalties import PrisonersPenalties

class PointsAttributor:
    def __init__(self) -> None:
        pass

    def attributePointsWhenTwoAreSilent(self) -> PrisonersPenalties:
        return PrisonersPenalties(-1, -1)

    def attributePointsWhenOneIsSilentAndSecondDenounces(self) -> PrisonersPenalties:
        return PrisonersPenalties(-10, 0)

    def attributePointsWhenOneDenouncesAndSecondIsSilent(self) -> PrisonersPenalties:
        return PrisonersPenalties(0, -10)

    def attributePointsWhenTwoDenouce(self) -> PrisonersPenalties:
        return PrisonersPenalties(-5, -5)

    def getPoints(self, prisonerOneDecision: Decision, prisonerTwoDecision: Decision) -> PrisonersPenalties:
        if prisonerOneDecision == Decision.IsSilent and prisonerTwoDecision == Decision.IsSilent:
            return self.attributePointsWhenTwoAreSilent()
        if prisonerOneDecision == Decision.IsSilent and prisonerTwoDecision == Decision.Denounces:
            return self.attributePointsWhenOneIsSilentAndSecondDenounces()
        if prisonerOneDecision == Decision.Denounces and prisonerTwoDecision == Decision.IsSilent:
            return self.attributePointsWhenOneDenouncesAndSecondIsSilent()
        if prisonerOneDecision == Decision.Denounces and prisonerTwoDecision == Decision.Denounces:
            return self.attributePointsWhenTwoDenouce()
