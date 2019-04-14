from tkinter import *
window = Tk()
window.title('Tic-Tac-Toe')

#Initial value
init = {'c':0}
o = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
x = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
clicked = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
def click(pos,loc):
    init['c']+=1
    loc = str(loc)
    if(init['c']%2==0):
        #Even Click
        if(clicked.get(loc)==0):
            #Valid Click
            pos['text'] = 'O'
            clicked[loc] = 1
            o[loc] = 1
            checkWinner()
        else:
            #Invalid Click
            messagebox.showinfo("Warning", "Invalid Click")
            init['c']-=1
    else:
        #Odd Clicks
        if(clicked.get(loc)==0):
            #Valid Click
            pos['text'] = 'X'
            clicked[loc] = 1
            x[loc] = 1
            checkWinner()
        else:
            #Invalid Click
            messagebox.showinfo("Warning", "Invalid Click")
            init['c']-=1

def checkWinner():
    print('Checking for pattern match')
    winnerPattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    Opattern = []
    Xpattern = []
    for i in o:
        if(o.get(i)==1):
            Opattern.append(int(i))
    for i in x:
        if(x.get(i)==1):
            Xpattern.append(int(i))
    patternMatch(winnerPattern,Opattern,'O')
    patternMatch(winnerPattern,Xpattern,'X')
    CheckGameState()

def patternMatch(a,b,player):
    for i in a:
        z=0
        for j in range(0,3):
            if(i[j] in b):
                z+=1
        if(z==3):
            msg = player + " Player Wins "
            print(msg)
            messagebox.showinfo("Winner!", msg)
            gameEnd()

def gameEnd():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def CheckGameState():
    a=0
    for i in clicked:
        a = clicked.get(i) + a
    if(a>=9):
        print("Draw match!")
        messagebox.showinfo("Winner", "Draw Game")
        gameEnd()
        
#Initializing buttons   
b1 = Button(window,text=" ",width=11,height=5,command=lambda : click(b1,1))
b2 = Button(window,text=" ",width=11,height=5,command=lambda : click(b2,2))
b3 = Button(window,text=" ",width=11,height=5,command=lambda : click(b3,3))
b4 = Button(window,text=" ",width=11,height=5,command=lambda : click(b4,4))
b5 = Button(window,text=" ",width=11,height=5,command=lambda : click(b5,5))
b6 = Button(window,text=" ",width=11,height=5,command=lambda : click(b6,6))
b7 = Button(window,text=" ",width=11,height=5,command=lambda : click(b7,7))
b8 = Button(window,text=" ",width=11,height=5,command=lambda : click(b8,8))
b9 = Button(window,text=" ",width=11,height=5,command=lambda : click(b9,9))

#Aligning buttons on grid
b1.grid(column=0,row=0)
b2.grid(column=1,row=0)
b3.grid(column=2,row=0)
b4.grid(column=0,row=1)
b5.grid(column=1,row=1)
b6.grid(column=2,row=1)
b7.grid(column=0,row=2)
b8.grid(column=1,row=2)
b9.grid(column=2,row=2)

