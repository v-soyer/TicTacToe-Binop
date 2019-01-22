#!/usr/bin/env python3

from display import printBoard
from check import *
from ia import iaPlay
from placePlay import placePlay

def main():
    playerBoard = 0
    iaBoard = 0
    printBoard(playerBoard, iaBoard)
    print("")
    endgame = checkIfWinner(playerBoard, iaBoard)

    while (not endgame):
        entry = input("Enter where you want to play: ")
        try:
            entry = int(entry)
        except:
            print ("You should enter a number between 0 and 8")
            continue
        if (entry < 0 or entry > 8):
            print ("You should enter a number between 0 and 8")
            continue
        if (checkIfAlreadyPlaced(entry, (playerBoard | iaBoard))):
            print("This place is already taken")
            continue
        playerBoard = placePlay(entry, playerBoard)
        printBoard(playerBoard, iaBoard)
        iaBoard = iaPlay(playerBoard, iaBoard)
        print("")
        print ("A.I. just played")
        printBoard(playerBoard, iaBoard)
        print("\n")
        endgame = checkIfWinner(playerBoard, iaBoard)

    if (endgame == 1):
        print("Human player has won !! \\o/ Congrats")
    else:
        print("A.I. Just beat you !! looser...")

if (__name__ == '__main__'):
    main()