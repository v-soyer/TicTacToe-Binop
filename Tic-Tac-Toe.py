#!/usr/bin/env python3

from display import printBoard
from check import *
from ia import iaPlay
from placePlay import placePlay
import random

def doVerification(playerBoard, iaBoard):
    endgame = checkIfWinner(playerBoard, iaBoard)
    if (endgame):
        return (endgame)
    if (checkPat(playerBoard, iaBoard) == 511):
        return (3)
    return (0)

def playerBegin(playerBoard, iaBoard):
    endgame = 0
    while (True):
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
        endgame = doVerification(playerBoard, iaBoard)
        if (endgame):
            break
        printBoard(playerBoard, iaBoard)
        iaBoard = iaPlay(playerBoard, iaBoard)
        endgame = doVerification(playerBoard, iaBoard)
        if (endgame):
            break
        print ("\nA.I. just played")
        printBoard(playerBoard, iaBoard)
        print("\n")
    print("\n")
    printBoard(playerBoard, iaBoard)
    print("")
    if (endgame == 1):
        print("Human player has won !! \\o/ Congrats")
    elif (endgame == 2):
        print("A.I. Just beat you !! looser...")
    else:
        print("PAT !")


def iaBegin(playerBoard, iaBoard):
    playerHasPlayed = 1
    while (True):
        if (playerHasPlayed):
            iaBoard = iaPlay(playerBoard, iaBoard)
            endgame = doVerification(playerBoard, iaBoard)
            if (endgame):
                break
            print ("\nA.I. just played")
            printBoard(playerBoard, iaBoard)
            print("\n")

        playerHasPlayed = 0
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
        playerHasPlayed = 1
        playerBoard = placePlay(entry, playerBoard)
        endgame = doVerification(playerBoard, iaBoard)
        if (endgame):
            break
        printBoard(playerBoard, iaBoard)
    print("\n")
    printBoard(playerBoard, iaBoard)
    print("")
    if (endgame == 1):
        print("Human player has won !! \\o/ Congrats")
    elif (endgame == 2):
        print("A.I. Just beat you !! looser...")
    else:
        print("PAT !")

def main():
    randval = random.randint(0, 1)
    playerBoard = 0
    iaBoard = 0
    printBoard(playerBoard, iaBoard)
    print("")

    if (randval == 0):
        playerBegin(playerBoard, iaBoard)
    else:
        iaBegin(playerBoard, iaBoard)

if (__name__ == '__main__'):
    main()