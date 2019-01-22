def wichPlayer(p1, p2, val):
    if (p1 & val):
        return ("X")
    elif (p2 & val):
        return ("O")
    else:
        return (" ")

def print1stLine(p1, p2):
    print(wichPlayer(p1, p2, 1), end="")
    print("|", end="")
    print(wichPlayer(p1,p2, 2), end="")
    print("|", end="")
    print(wichPlayer(p1,p2, 4))

def print2ndLine(p1, p2):
    print(wichPlayer(p1, p2, 8), end="")
    print("|", end="")
    print(wichPlayer(p1,p2, 16), end="")
    print("|", end="")
    print(wichPlayer(p1,p2, 32))

def print3rdLine(p1, p2):
    print(wichPlayer(p1, p2, 64), end="")
    print("|", end="")
    print(wichPlayer(p1,p2, 128), end="")
    print("|", end="")
    print(wichPlayer(p1,p2, 256))

def printBoard(p1, p2):
    print1stLine(p1, p2)
    print("-+-+-")
    print2ndLine(p1, p2)
    print("-+-+-")
    print3rdLine(p1, p2)