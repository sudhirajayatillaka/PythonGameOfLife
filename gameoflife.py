from tkinter import *
import random
from numpy import random
import math

vres = 1000
hres = 1000

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
            if liveneighbors < 2 or liveneighbors > 3:
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
            rnd_board[i][j] = random.choice([0, 1], p=[0.5, 0.5]).item()
    
    return rnd_board

board = rnd_board(int(hres/10),int(vres/10))

root = Tk()
root.title("Game Of Life")
root.configure(background='black')

def draw_board():
    isdead = True
    global board
    #print(board)
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
            C.create_rectangle(j*10, i*10, j*10+10, i*10+10, fill=fill_color , outline = 'gray')
    if isdead:
        board = rnd_board(int(hres/10),int(vres/10))
    else:
        board = update_board(board)
    C.after(100,draw_board)


def new_board(event):
    global board
    board = rnd_board(int(hres/10),int(vres/10))

def left_click(event):
    global board
    #print(event)
    xcord = math.floor(event.x/10)
    ycord = math.floor(event.y/10)
    print("X : ", xcord, " Y : ", ycord)


C = Canvas(root, bg="Black", height=hres, width=vres)

C.bind("<Button-3>", new_board)
C.bind("<Button-1>", left_click)

C.pack()
draw_board()
root.mainloop()
