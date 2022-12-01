from tkinter import *
from time import sleep



#SinglePlayer Frame
def single():
    hide_frames()
    single_frame.pack(fill='both',expand=1)
    heading = Label(single_frame,text ='Alone').pack()

#Multiplayer Frame
def multi():
    hide_frames()
    multi_frame.pack(fill='both',expand=1)
    heading = Label(multi_frame, text ='w Frends').pack()


# HOme Frame
def home():
    hide_frames()
    start_frame.pack(fill='both',expand =1 )

# hide prev frames
def hide_frames():
    multi_frame.pack_forget()
    single_frame.pack_forget()
    start_frame.pack_forget()

root = Tk()
root.title('SUTD Fued')
mymenu = Menu(root)
root.geometry('500x500')
root.config(menu = mymenu)
mymenu.add_command(label = 'alone', command = single)
mymenu.add_command(label = 'w frends', command = multi)
mymenu.add_command(label = 'home', command = home)



#FRAMES (something like divs in html)
start_frame = Frame(root, width=500,height=500) #home page
start_frame.pack(fill='both',expand=1)
multi_frame = Frame(root, width=500,height=500) #page for multiplayer
single_frame = Frame(root, width=500,height=500) #page for singleplayer




heading_text = Label(start_frame,text = 'Welcome to SUTD Feud',font=('Helvetica',25)).pack(pady=20)
# Singlepayer button
btn1 = Button(start_frame,command= single , text='alone lol').pack()
# multiplayer button
btn2 =Button(start_frame, command = multi, text='u have friends').pack()






















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
