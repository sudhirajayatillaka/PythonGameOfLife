# from tkinter import *

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

board = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

while True:
    print(board)
    board = update_board(board)

'''
root = Tk()
a = Label(root, text ="Hello World")
a.pack()

root.mainloop()
'''