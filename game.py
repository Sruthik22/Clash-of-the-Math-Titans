import tkinter as tk
win=tk.Tk()

# Usage example for pyaudio and AudioFile class
# YOUR FILE PATH WILL BE DIFFERENT


#4x4 grid
#box size is 100 by 100

win.resizable(False,False)
#starts At 1,1
Difficulty=1# 1 to 10

        
screenmode=0
fontsizeone1=18
fontsizetwo2=25
font=""
nowmode=100

def deleteallitems():
    for child in win.winfo_children():
        child.destroy()

from random import randint
world=[ [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
world[randint(0,3)][3]=1
world[randint(0,3)][0]=3

world[randint(0,3)][1]=2

world[randint(0,3)][2]=2
        #0 is nothing,i is player,2 is bag guy ,3 is goal
keythatwaspressed='none'
def getrandomop():
    if(Difficulty>6):
        num=randint(0,3)
    else:
        num=randint(0,2)

    if (num==0):
        return('+')
    elif (num==1):
        return('-')
    elif (num==2):
        return('*')
    else:
        return('/')
def drawgrid():
    for i in range(4):#ys
        for p in range(4):#xs
            can.create_rectangle(i*100+5,p*100+5,i*100+100+5,p*100+100+5)
            if(world[i][p]==1):
                can.create_oval(i*100+5,p*100+5,i*100+100+5,p*100+100+5,fill="Blue")
            elif(world[i][p]==2):
                can.create_rectangle(i*100+5+10,p*100+5+10,i*100+100+5-10,p*100+100+5-10,fill="red")
                can.create_rectangle(i*100+5+30,p*100+5+30,i*100+100+5-60,p*100+100+5-60,fill="red")
                can.create_rectangle(i*100+5+60,p*100+5+30,i*100+100+5-30,p*100+100+5-60,fill="red")
                can.create_rectangle(i*100+5+20,p*100+5+70,i*100+100+5-20,p*100+100+5-20,fill="red")
            elif(world[i][p]==3):
                can.create_rectangle(i*100+5+15,p*100+5+10,i*100+5+20,p*100+100+5-10,fill="green")
                
                can.create_rectangle(i*100+5+15,p*100+5+10,i*100+100+5-15,p*100+100+5-50,fill="green")
                # world

import random
numbers = [random.randint(0,5), random.randint(0,5), random.randint(0,5), random.randint(0,5)]
print (numbers)
win_state = False
correct_number=eval(str(numbers[0])+getrandomop()+str(numbers[1])+getrandomop()+str(numbers[2])+getrandomop()+str(numbers[3]))
write_text=1

def buttonenterevent():
    global win_state
    global keythatwaspressed
    global world
    global write_text
    global screenmode
    #if(eval(str(numbers[0])+item1.get()+str(numbers[1])+item2.get()+str(numbers[2])+item3.get()+str(numbers[3]))==correct_number):
    if(True):
        win_state = True
        keythatwaspressed="none"
        print("COrrect!");
        write_text=2
        Draw()
        while (keythatwaspressed=='none'):
            win.update()
        print("Keyed!!");
        breakloop=False
        
        for y in range(4):
            for x in range(4):
                if(world[y][x]==1):
                    world[y][x]=0
                    print("Found!!");
                    if(keythatwaspressed=="Up"):
                        if(world[y ][x- 1]==3):
                            screenmode=3
                        if(world[y ][x- 1]==2):
                            screenmode=4;
                    if(keythatwaspressed=="Down"):
                        if(world[y ][x+ 1]==3):
                            screenmode=3
                        if(world[y ][x+ 1]==2):
                            screenmode=4;
                    if(keythatwaspressed=="Right"):
                        if(world[y+1 ][x]==3):
                            screenmode=3
                        if(world[y+1 ][x]==2):
                            screenmode=4;
                    if(keythatwaspressed=="Left"):
                        if(world[y-1 ][x]==3):
                            screenmode=3
                        if(world[y-1 ][x]==2):
                            screenmode=4;
                    try:
                        
                        if(keythatwaspressed=="Up"):
                            world[y ][x- 1]=1
                        if(keythatwaspressed=="Down"):
                            world[y][x + 1]=1
                        if(keythatwaspressed=="Right"):
                            world[y + 1][x ]=1
                        if(keythatwaspressed=="Left"):
                            world[y- 1 ][x]=1
                    except:
                        world[y][x]=1

                    breakloop=True
                    break
            if(breakloop):
                break
        write_text=1
        global numbers
        global correct_number
        numbers = [random.randint(0,1+Difficulty*4), random.randint(0,1+Difficulty*4), random.randint(0,1+Difficulty*4), random.randint(0,1+Difficulty*4)]
        correct_number=eval(str(numbers[0])+getrandomop()+str(numbers[1])+getrandomop()+str(numbers[2])+getrandomop()+str(numbers[3]))

        Draw()
        win_state=False
def key(event):
    global keythatwaspressed
    global win_state
    if(win_state):
        keythatwaspressed= event.keysym

    
def Draw():
    deleteallitems()
    global can
    can=tk.Canvas(win,width=410,height=500)
    can.pack()
    
    global item1
    global item2
    global item3
    global write_text
    can.delete('all')
    drawgrid() 
    if(write_text==1):
        can.create_text(410/2,420,text="Select the right operations to get the number "+str(correct_number),fill='black',font=(font,fontsizeone1))
    else:
        can.create_text(410/2,420,text="Use the arrow keys to move",fill='black',font=(font,fontsizeone1))

    can.create_text(410/2,450,text=(str(numbers[0])+" "*8+str(numbers[1])+" "*8+str(numbers[2])+" "*8+str(numbers[3])),fill='grey',font=("",fontsizetwo2))
    #can.create_rectangle(410/2,450,410/2,450+30-15)
    if(Difficulty>6):
        item3 = tk.StringVar(win)
        item3.set("+") # default value
        w = tk.OptionMenu(win, item3, "+", "-", "*","/")
        can.create_window(255,440,anchor = tk.NW, window = w)
        
        item2 = tk.StringVar(win)
        item2.set("+") # default value
        w = tk.OptionMenu(win, item2, "+", "-", "*","/")
        can.create_window(255-70,440,anchor = tk.NW, window = w)
        
        item1 = tk.StringVar(win)
        item1.set("+") # default value
        w = tk.OptionMenu(win, item1, "+", "-", "*","/")
        can.create_window(255-140,440,anchor = tk.NW, window = w)
        
        enterbutton = tk.Button(win, text="OK", command=buttonenterevent)
        can.create_window(410/2,480,anchor = tk.NW, window = enterbutton)
    else:
    
        item3 = tk.StringVar(win)
        item3.set("+") # default value
        w = tk.OptionMenu(win, item3, "+", "-", "*")
        can.create_window(255,440,anchor = tk.NW, window = w)
    
        item2 = tk.StringVar(win)
        item2.set("+") # default value
        w = tk.OptionMenu(win, item2, "+", "-", "*")
        can.create_window(255-70,440,anchor = tk.NW, window = w)
        
        item1 = tk.StringVar(win)
        item1.set("+") # default value
        w = tk.OptionMenu(win, item1, "+", "-", "*")
        can.create_window(255-140,440,anchor = tk.NW, window = w)
        
        enterbutton = tk.Button(win, text="OK", command=buttonenterevent)
        can.create_window(410/2,480,anchor = tk.NW, window = enterbutton)
def drawstart():
    #4by4grid
    #box size is 100 by 100
    can=tk.Canvas(win,width=500,height=500)
    can.pack()
    win.resizable(False,False)
    can.create_text(250,100,text = "Clash of the math titans", fill = 'black', font = ("",30))
    can.create_rectangle(100,200,400,300)
    can.create_text(250,250,text = "Play", fill = 'black', font = ("",25))
    can.create_rectangle(100,450,400,350)
    can.create_text(250,400,text = "Settings", fill = 'black', font = ("",25))
def optionsscreen():
    global d1
    global el
    global f1
    global fontfamily
    global sound
    global difficulty
    sound = tk.IntVar()
    fontfamily = tk.StringVar(win)
    
    fontfamily.set("Arial")
    d1 = tk.Entry(win, text="Font Size 1")
    f1 = tk.Entry(win, text="Font Size 2")
    difficulty= tk.Entry(win, text="Difficulty:")
    
    e1 = tk.OptionMenu(win, fontfamily, "Arial", "Courier New", "Comic Sans MS", "Fixedsys", "MS Sans Serif", "MS Serif", "Symbol", "System", "Verdana")
    x1=tk.Text(win,width=12,height=1)
    y1=tk.Text(win,width=12,height=1)
    difficultytext=tk.Text(win,width=12,height=1)
    x1.insert(0.0,"font size 1:")
    difficultytext.insert(0.0,"difficulty:")
    y1.insert(0.0,"font size 2:")
    
    x1.config(state=tk.DISABLED)
    y1.config(state=tk.DISABLED)
    difficultytext.config(state=tk.DISABLED)
    d1.grid(row=1,column=2)
    f1.grid(row=1,column=3)
    e1.grid(row=1,column=4)
    d1.delete(0,'end')
    d1.insert(0,fontsizeone1)
    f1.delete(0,'end')
    f1.insert(0,fontsizetwo2)
    difficulty.delete(0,'end')
    difficulty.insert(0,Difficulty)
    x1.grid(row=3,column=2)
    x1.pack(fill=tk.X)
    
    y1.grid(row=3,column=3)
    d1.pack(fill=tk.X)
    y1.pack(fill=tk.X)
    
    f1.pack(fill=tk.X)
    
    e1.pack(fill=tk.X)
    difficultytext.pack(fill=tk.X)
    backbutton=tk.Button(win,text="Home",command=Home2)
    difficulty.pack(fill=tk.X)
    backbutton.pack()
    
def Home2():
    global screenmode
    global Difficulty
    global difficulty
    global el
    global d1
    global f1
    global fontfamily
    global fontsizeone1
    global fontsizeone2
    screenmode=0
    try:
        Difficulty=int(difficulty.get())
        fontsizeone1=int(d1.get())
        fontsizeone2=int(d2.get())
        el
    except:
        pass
def Home():
    global screenmode
    screenmode=0
def WinScreen():
    global world
    world=[ [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    world[randint(0,3)][3]=1
    world[randint(0,3)][0]=3

    world[randint(0,3)][1]=2

    world[randint(0,3)][2]=2
    can=tk.Canvas(win,width=500,height=500)
    can.pack()
    win.resizable(False,False)
    can.create_text(250,250,text = "You win!", fill = '#55B7FF', font = ("",60))
    can.configure(background='#7A5EFF')
    
    enterbutton = tk.Button(win, text="Home",command=Home)
    enterbutton.configure(activebackground = '#7A5EFF',width=10,height=2)
    
    can.create_window(410/2,300,anchor = tk.NW, window = enterbutton)
def losescreen():
    global world
    world=[ [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    world[randint(0,3)][3]=1
    world[randint(0,3)][0]=3

    world[randint(0,3)][1]=2

    world[randint(0,3)][2]=2
    can=tk.Canvas(win,width=500,height=500)
    can.pack()
    win.resizable(False,False)
    can.create_text(250,250,text = "You Lose", fill = 'red', font = ("",30))
    can.configure(background='black')
    backbutton = tk.Button(win, text="Home",command=Home)
    backbutton.configure(activebackground = '#7A5EFF',width=10,height=2)
    
    can.create_window(410/2,300,anchor = tk.NW, window = backbutton)

def mouseclick(event):
    global screenmode
    if(nowmode==0 and event.x>100 and event.x<400):
        if(event.y>200 and event.y<300):
            screenmode=1
        if(event.y>350 and event.y<450):
            screenmode=2
win.bind("<Key>", key)
win.bind("<Button-1>", mouseclick)

while 1:
    if(nowmode!=screenmode):
        deleteallitems()
        nowmode=screenmode
        if(screenmode==0):
            drawstart()
        if(screenmode==1):
            Draw()
        if(screenmode==2):
            optionsscreen()
        if(screenmode==3):
            WinScreen()
        if(screenmode==4):
            losescreen()
    win.update()



