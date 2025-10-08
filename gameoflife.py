from tkinter import *
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

board = rnd_board(100,100)

root = Tk()
root.title("Game Of Life")

def draw_board():
    isdead = True
    global board
    print(board)
    C.delete("all")
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                fill_color = "white"
                isdead = False
            else:
                fill_color = "black"
            C.create_rectangle(j*10, i*10, j*10+10, i*10+10, fill=fill_color , outline = 'white')
    if isdead:
        board = rnd_board(100,100)
    else:
        board = update_board(board)
    C.after(100,draw_board)


def new_board(event):
    global board
    board = rnd_board(100,100)

    

C = Canvas(root, bg="Black", height=1000, width=1000)

C.bind("<Button-3>",new_board)

C.pack()
draw_board()
root.mainloop()
