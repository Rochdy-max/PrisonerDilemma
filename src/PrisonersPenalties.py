##
## EPITECH PROJECT, 2023
## LiveCoding [WSL : Ubuntu20.04]
## File description:
## PrisonerPenalties
##

class PrisonersPenalties:
    def __init__(self, prisonerOnePenalty = 0, prisonerTwoPenalty = 0) -> None:
        self.prisonerOnePenalty = prisonerOnePenalty
        self.prisonerTwoPenalty = prisonerTwoPenalty

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, PrisonersPenalties):
            return self.prisonerOnePenalty == __o.prisonerOnePenalty and self.prisonerTwoPenalty == __o.prisonerTwoPenalty
        if isinstance(__o, tuple[int, int]):
            return self.prisonerOnePenalty == __o[0] and self.prisonerTwoPenalty == __o[1]
        return False
