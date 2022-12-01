from tkinter import *
from time import sleep


'''
Starter Page that introduces us the game!
'''


#SinglePlayer
def single():
    pass

#Multiplayer
def multi():
    pass


root = Tk()
root.geometry("800x500")
root.title('SUTD Fued')

heading_frame = Label(text = 'Welcome to SUTD Feud',font=('Helvetica',25)).pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

# Singlepayer button
# multiplayer button
btn1 = Button(button_frame, )

















'''



used to select game mode : 
singleplayer - j by urself lorh.

Multiplayer - against 2 players or 2 group of players


def modepage():
    global modep
    modep = Toplevel()
    modep.title('Game Mode')
    modep.geometry("800x500")
    btn2 = Button(modep,text ='Single Player', command =gamepage1).pack()
    btn3 = Button(modep,text ='Multiplayer', command =gamepage2).pack()




def gamepage1():
    gpage1 = Toplevel()
    gpage1.title('SUTD Feud Alone LOL')
    gpage1.geometry("800x500")
    modep.destroy()
    btn4 = Button(modep,text ='Go back', command =modepage).pack()

    gamepage1.destroy

def gamepage2():
    gpage2 = Toplevel()
    gpage2.title('SUTD Feud Alone LOL')
    gpage2.geometry("800x500")
    modep.destroy()

def endwindow():
    pass

'''

mainloop()
