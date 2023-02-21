# importing requried libraries
from tkinter import *
from PIL import Image, ImageTk
import random


# variables to store score of user and computer
userscore = 0
pcscore = 0

# functions to handle all the events that will be triggered while making choises
def enter(event):
    rock.config(bg = 'black', fg = 'white')
def enter2(event):
    paper.config(bg = 'black', fg = 'white')
def enter3(event):
    scissor.config(bg = 'black', fg = 'white')
def leave(event):
    rock.config(bg = 'white', fg = 'black')
def leave1(event):
    paper.config(bg = 'white', fg = 'black')
def leave2(event):
    scissor.config(bg = 'white', fg = 'black')
def entergame(event):
    maingame()

# Maingame Function will bring a new window of GUI and will provide a platform
# to play rock paper scissor
def maingame():
    global userscore, pcscore
    global nameinp
    global rock, paper, scissor

    # to set the size of the tkinter window we use geometry() function
    root.geometry('650x750')
    # used destroy funtion to destroy all the widgets on the screen
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()

    # below lines will display the scores of both user and pc
    # grid() in tkinter is used to place the labels of the scores
    L2 = Label(text = f"{nameinp.get()} Score: {userscore}", bg = '#4834DF',
               fg = '#ffffff', borderwidth = 5, relief = RAISED,
               font = 'Rockwell 13 bold', padx = 4, pady = 2)
    L2.grid(row = 6, column = 0, pady = 15)
    L3 = Label(text = f"PC Score: {pcscore}", bg = '#4834DF',
               fg = '#ffffff', borderwidth = 5, relief = RAISED,
               font = 'Rockwell 13 bold', padx = 4, pady = 2)
    L3.grid(row = 7, column = 0, pady = 15)






    
