# importing requried libraries
from tkinter import *
# from PIL import Image, ImageTk
import random


# variables to store score of user and computer
userscore = 0
pcscore = 0

# functions to handle all the events that will be triggered while making choises
def enter(event):
    rock.config(bg = 'black', fg = 'white')
def enter1(event):
    paper.config(bg = 'black', fg = 'white')
def enter2(event):
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

    # this function handles the click events
    def click(event):
        global userscore, pcscore
        global L1
        global pcchose
        # grid_forget() to remove the other labels properly
        L1.grid_forget()
        # to destroy the selected labels
        pcchose.destroy()

        # this will take the text of button
        val = event.widget.cget('text')

        # to make a random selection for the computer
        x = random.randint(0, 2)
        l1 = ['Rock', 'Paper', 'Scissor']
        # pc's choice
        pc_opt = l1[x]

        # pc's choice will be displayed in the form of a label
        pcchose = Label(text = f'PC Opted: {pc_opt}', font = 'lucida 15 bold',
                        bg = 'black', fg = 'red')
        pcchose.grid(row = 6, column = 1, pady = 15)


        ### actual logic of the rock, paper, scissor
        # val holds user's choice and pc_opt holds pc's choice

        # user - rock; pc - paper
        if val == 'Rock' and pc_opt == 'Paper':
            L1 = Label(text = 'PC Won', font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
            pcscore += 1

        # user - rock; pc - scissor
        elif val == 'Rock' and pc_opt == 'Scissor':
            L1 = Label(text = f'{nameinp.get()} Won', font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
            userscore += 1

        # user - paper; pc - scissor
        elif val == 'Paper' and pc_opt == 'Scissor':
            L1 = Label(text = 'PC Won', font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
            pcscore += 1

        # user - paper; pc - rock
        elif val == 'Paper' and pc_opt == 'Rock':
            L1 = Label(text = f'{nameinp.get()} Won', font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
            userscore += 1

        # user - scissor; pc - rock
        elif val == 'Scissor' and pc_opt == 'Rock':
            L1 = Label(text = 'PC Won', font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
            pcscore += 1

        # user - scissor; pc - paper
        elif val == 'Scissor' and pc_opt == 'Paper':
            L1 = Label(text = f'{nameinp.get()} Won', font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
            userscore += 1

        # user choice == pc choice
        elif val == pc_opt:
            L1 = Label(text = "It's A Tie", font = 'lucida 15 bold',
                       bg = 'black', fg = 'gold')
            L1.grid(row = 7, column = 1, pady = 15)
        maingame()

    # overall layout of the RPS Game
    head = Label(text = 'Rock Paper Scissor', font = 'arial 35 bold',
                 bg = "black", fg = "white")
    head.grid(columnspan = 2, row = 0, ipadx = 70, padx = 33, pady = 10)
    playerone = Label(text = f"Player 1 : {nameinp.get()}", font = "lucida 16")
    playerone.grid(row = 2, column = 0)
    playertwo = Label(text = f"Player 2 : Computer", font = "lucida 16")
    playertwo.grid(row = 2, column = 1)

    # set of buttons available for player1
    rock = Button(text = "Rock", font = 'comicsansms 14 bold',
                    height = 1, width = 7)
    rock.grid(row = 3, column = 0, pady = 15)
    # bind() to bind multiple functions in the program
    rock.bind('<Enter>', enter)
    rock.bind('<Leave>', leave)
    rock.bind('<Button-1>', click)
    paper = Button(text = "Paper", font = 'comicsansms 14 bold',
                    height = 1, width = 7)
    paper.grid(row = 4, column = 0, pady = 15)
    # bind() to bind multiple functions in the program
    paper.bind('<Enter>', enter1)
    paper.bind('<Leave>', leave1)
    paper.bind('<Button-1>', click)
    scissor = Button(text = "Scissor", font = 'comicsansms 14 bold',
                    height = 1, width = 7)
    scissor.grid(row = 5, column = 0, pady = 15)
    # bind() to bind multiple functions in the program
    scissor.bind('<Enter>', enter2)
    scissor.bind('<Leave>', leave2)
    scissor.bind('<Button-1>', click)

    #set of buttons for the computers
    rock1 = Button(text = "Rock", font = 'comicsansms 14 bold',
                    height = 1, width = 7)
    rock1.grid(row = 3, column = 1, pady = 15)
    paper1 = Button(text = "Paper", font = 'comicsansms 14 bold',
                    height = 1, width = 7)
    paper1.grid(row = 4, column = 1, pady = 15)
    scissor1 = Button(text = "Scissor", font = 'comicsansms 14 bold',
                    height = 1, width = 7)
    scissor1.grid(row = 5, column = 1, pady = 15)

    # button to close the Game
    # it will destroy all the widgets used in the Game
    btnclose = Button(text = "Close Game", command = root.destroy,
                       bg = "green", font = "arial 10 bold")
    btnclose.place(x = 300, y = 410)


### now the actual programming of the GUI
### main function of the project
#if __name__ == "__main__":
root = Tk()
root.title("Rock Paper Scissor")
root.wm_iconbitmap("play.png")
root.geometry("650x750")
root.maxsize
root.minsize(650, 450)

# defining widgets to use them in different functions
rock = Button()
paper = Button()
scissor = Button()

# defining label to use it later in program
L1 = Label()
pcchose = Label()

# lauch page of the Game
f1 = Frame(root)
# img = Image.open('symbols.png')
# img = img.resize((650, 450), Image.ANTIALIAS)
# pic = ImageTk.PhotoImage(img)
# Lab = Label(f1, image = pic)
# Lab.pack()
f1.pack()

# label for user name input
name = Label(root, text = 'Enter Your Name: ', font = "arial 15 bold")
name.place(x = 262, y = 250)

# variable to store username and use it further
nameinp = StringVar()
inpname = Entry(root, textvar = nameinp, font = "arial 15 bold")

# we bind Return event with inpname entry widget i.e. if enter key is pressed
# then entergame function will be called
inpname.bind('<Return>', entergame)
inpname.place(x = 275, y = 290)

# a button of lets play is added so that the user can enter the main game window
sub = Button(root, text = "Let's Play", font = "lucida 10 bold",
                bg = "black", fg = "white", command = maingame)
sub.place(x = 305, y = 350)

# tkinter mainloop() function that will call the main window of tkinter
root.mainloop()
