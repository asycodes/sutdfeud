from tkinter import *


#file1 = open('feuddata/singlenames.txt')


# ----------HOme Frame----------
def home():
    hide_frames()
    start_frame.pack(fill='both',expand =1 )

#----------SinglePlayer Frame----------
def single():
    hide_frames()
    single_frame.pack(fill='both',expand=1)
    heading = Label(single_frame,text ='Alone').pack()
    textbox = Text(single_frame,width=40,height=10,background= "gray71",foreground="#fff",font= ('Sans Serif', 13, 'italic bold'))
    textbox.insert(INSERT,"Your name")
    textbox.pack()
    btn3 = Button(single_frame,text='Enter',command=singlematch(textbox.get('1.0',END))) #get their name
    btn3.pack() # proceed to the game

def singlematch(name='none'):
    hide_frames()
    mylabel = Label(singlematch_frame,text='').pack()
    singlematch_frame.pack(fill='both',expand=1)
    

    
    

#---------Multiplayer Frame----------
def multi():
    hide_frames()
    multi_frame.pack(fill='both',expand=1)
    heading = Label(multi_frame, text ='w Frends').pack()
    textbox1 = Text(multi_frame,width=40,height=10,font= ('Sans Serif', 13, 'italic bold'))
    textbox2 = Text(multi_frame,width=40,height=10,font= ('Sans Serif', 13, 'italic bold'))
    textbox1.insert(INSERT,"Name for Group 1")
    textbox2.insert(INSERT,"Name for Group 2")
    textbox1.pack()
    textbox2.pack()
    btn3 = Button(multi_frame,text='Enter',command=get_text) #get their name
    btn3.pack() # proceed to the game

def multimatch():
    pass 

# ----------hide prev frames----------
'''everytime u add a new frame/page, u have to update here'''
def hide_frames():
    # to hide multiple iterations of the same frames
    for widget in multi_frame.winfo_children():
        widget.destroy()
    for widget in single_frame.winfo_children():
        widget.destroy()
    # to hide previous frames 
    multi_frame.pack_forget()
    single_frame.pack_forget()
    start_frame.pack_forget()
    singlematch_frame.pack_forget()

def get_text():
    pass




#---------underneath here is the initialization-----------

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
multi_frame = Frame(root, width=500,height=500) #page for multiplayer
single_frame = Frame(root, width=500,height=500) #page for singleplayer
singlematch_frame = Frame(root, width=500,height=500)
start_frame.pack(fill='both',expand=1)



#header
heading_text = Label(start_frame,text = 'Welcome to SUTD Feud',font=('Helvetica',25)).pack(pady=20)
# Singlepayer button
btn1 = Button(start_frame,command= single , text='alone lol').pack()
# multiplayer button
btn2 =Button(start_frame, command = multi, text='u have friends').pack()



mainloop()
