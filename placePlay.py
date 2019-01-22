def placePlay(entry, board):
    if (entry == 0):
        board = board ^ 1
    if (entry == 1):
        board = board ^ 2
    if (entry == 2):
        board = board ^ 4
    if (entry == 3):
        board = board ^ 8
    if (entry == 4):
        board = board ^ 16
    if (entry == 5):
        board = board ^ 32
    if (entry == 6):
        board = board ^ 64
    if (entry == 7):
        board = board ^ 128
    if (entry == 8):
        board = board ^ 256
    return (board)