#!/bin/python3

from sys import argv, stderr
from PrisonerDilemmaGame import PrisonerDilemmaGame

USAGE = ""

def main(ac, av):
    if ac == 2 and av[1] == "-h":
        print(USAGE)
        return 0
    game = PrisonerDilemmaGame()
    game.play()
    game.reviewParty()
    return 0

if __name__ == "__main__":
    av = argv
    ac = len(av)
    status = main(ac, av)
    exit(status)
