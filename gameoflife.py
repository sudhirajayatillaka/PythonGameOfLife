# from tkinter import *
import time
import random

def update_board(board):
    row = len(board)
    col = len(board[0])
    newboard = [[0] * col for i in range(row)]
    for i in range(row):
        for j in range(col):
            liveneighbors = 0
            for x in range(max(0, i - 1), min(row, i + 2)):
                for y in range(max(0, j - 1), min(col, j + 2)):
                    if (x != i or y != j) and board[x][y] == 1:
                        liveneighbors += 1
            if liveneighbors < 2 and liveneighbors > 3:
                newboard[i][j] = 0
            if liveneighbors == 3:
                newboard[i][j] = 1
            if liveneighbors == 2 and newboard[i][j] == 1:
                newboard[i][j] = 1
    return newboard


def rnd_board(ncol,nrow):
    rnd_board = [[0] * ncol for i in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            rnd_board[i][j] = random.randint(0, 1)
    
    return rnd_board

board = rnd_board(10,10)

while True:
    print(board)
    board = update_board(board)
    time.sleep(1)

'''
root = Tk()
a = Label(root, text ="Hello World")
a.pack()

root.mainloop()
'''