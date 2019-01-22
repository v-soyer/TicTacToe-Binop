def checkDiag(board):
    if (board & 273 == 273):
        return (1)
    if (board & 84 == 84):
        return (1)
    return (0)


def checkHorizon(board):
    if (board & 448 == 448):
        return 1
    if (board & 56 == 56):
        return 1
    if (board & 7 == 7):
        return 1
    return (0)


def checkVertical(board):
    if (board & 292 == 292):
        return 1
    if (board & 146 == 146):
        return 1
    if (board & 73 == 73):
        return 1
    return (0)


def checkIfAlreadyPlaced(entry, board):
    if (entry == 0):
        return (board & 1)
    if (entry == 1):
        return (board & 2)
    if (entry == 2):
        return (board & 4)
    if (entry == 3):
        return (board & 8)
    if (entry == 4):
        return (board & 16)
    if (entry == 5):
        return (board & 32)
    if (entry == 6):
        return (board & 64)
    if (entry == 7):
        return (board & 128)
    if (entry == 8):
        return (board & 256)
    return (0)


def checkIfWinner(p1Board, iaBoard):
    if (checkDiag(p1Board)):
        return (1)
    if (checkHorizon(p1Board)):
        return (1)
    if (checkVertical(p1Board)):
        return (1)

    if (checkDiag(iaBoard)):
        return (2)
    if (checkHorizon(iaBoard)):
        return (2)
    if (checkVertical(iaBoard)):
        return (2)
    return (0)

def checkPat(playerBoard, iaBoard):
    return (playerBoard | iaBoard)