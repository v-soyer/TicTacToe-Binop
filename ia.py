from check import *
from placePlay import placePlay
import random

def iaPlay(playerBoard, iaBoard):
    val = random.randint(0, 8)
    while (checkIfAlreadyPlaced(val, playerBoard | iaBoard)):
        val = random.randint(0, 8)
    iaBoard = placePlay(val, iaBoard)
    return (iaBoard)
