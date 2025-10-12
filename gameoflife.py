from tkinter import *
import random
from numpy import random
import math

vres = 1000
hres = 1000

auto = True

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
                print("i : ", i, " j : ", j, " Dead")
            if liveneighbors == 3:
                newboard[i][j] = 1
                print("i : ", i, " j : ", j, " Alive")
            if liveneighbors == 2 and board[i][j] == 1:
                newboard[i][j] = 1
                print("i : ", i, " j : ", j, " Alive")
    return newboard


def rnd_board(ncol,nrow):
    rnd_board = [[0] * ncol for i in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            rnd_board[i][j] = random.choice([0, 1], p=[0.9, 0.1]).item()
    
    return rnd_board

def cl_board(ncol,nrow):
    cl_board = [[0] * ncol for i in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            cl_board[i][j] = 0
    
    return cl_board

board = cl_board(int(hres/10),int(vres/10))

root = Tk()
root.title("Game Of Life")
root.configure(background='black')

def draw_board():
    global board
    #print(board)
    C.delete("all")
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                fill_color = "white"
            else:
                fill_color = "black"
            C.create_rectangle(j*10, i*10, j*10+10, i*10+10, fill=fill_color , outline = 'gray')

    if(auto):
        board = update_board(board)
        C.after(100,draw_board)


def new_board(event):
    global board
    board = rnd_board(int(hres/10),int(vres/10))
    draw_board()

def left_click(event):
    global board
    #print(event)
    xcord = math.floor(event.x/10)
    ycord = math.floor(event.y/10)
    print("X : ", xcord, " Y : ", ycord)
    if board[ycord][xcord] == 1:
        board[ycord][xcord] = 0
    else:
        board[ycord][xcord] = 1
    C.after(10,draw_board)
    

def next_gen(event):
    global board
    board = update_board(board)
    draw_board()


C = Canvas(root, bg="Black", height=hres, width=vres)

C.bind("<Button-3>", new_board)
C.bind("<Button-2>", next_gen)
C.bind("<Button-1>", left_click)
C.bind("<B1-Motion>", left_click)

C.pack()
draw_board()
root.mainloop()
