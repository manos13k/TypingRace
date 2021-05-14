from tkinter import *
import random
from tkinter.ttk import *


sentences = ["They're really good this year, aren't they?","Do you spend much time writing email?","I appreciated your help.","Follow me.","It's about time we went to bed.","No problem. What are you looking for?","Where's the mail box?","I can't keep doing this."],"You remind me of my mother.","We go there often.","I hear you are good at cooking.","You should spend less time complaining and more time doing something productive.","Mary and I have been acquainted with each other for many years.","You must not touch the paintings.","Please move your car out of here.","She surprised him with a kiss.","He has been sick in bed all week.","Nancy looks so tired.","That'd be really cool. I'd like to be a translator too.","I forgot the key and went back for it.","She was advised by him to give up smoking.","I went to the zoo yesterday.","I don't feel much like talking right now.","Can you handle it?","No matter how hard I try, I can't do it any better than she can.","She felt like crying.","I left the rest to him and went out.","Hi, is Mrs. Smith there, please?","I have a bad pain in my lower back."

win = Tk()
win.title("Typing Race")
win.geometry("600x200")
win.configure(background = "#174966")

timeleft = 120
x = 0

Instructionslbl= Label(win,justify = CENTER,foreground = "#69BFFF", background = "#174966", font=('Helvetica', 10,"bold"),text = "Type the sentence shown as fast as you can \n Hit <0> to Start \n and <ENTER> to confirm your answer \n You have excactly 2 minutes to submit your answer \n +1 point if you do it right")
Instructionslbl.grid(column = 0 , row = 0)
txt = Entry(win, width = 70,font=('Helvetica', 15,"bold"),foreground = "#367DA6")
txt.grid(column = 0, row= 2,columnspan = 100)

ransent = random.choice(sentences)

sentlbl = Label(win,text = ransent, justify = CENTER, borderwidth=20, relief="groove", font=('Helvetica', 15,"bold"),background= "#174966",foreground = "#69BFFF")
sentlbl.grid(column = 0 , row = 1,columnspan = 3)
timelbl = Label (win, text = "Time Left: " + str(timeleft), font=('Helvetica', 10,"bold"),background = "#174966",foreground = "#69BFFF", borderwidth=5, relief="groove")
timelbl.grid(column = 2, row = 0)
pointslbl = Label(win,text ="Score:" + str(x), font=('Helvetica', 10,"bold"), borderwidth=5, relief="groove",background = "#174966",foreground = "#69BFFF")
pointslbl.grid(column = 3, row= 0)

def countdown():
    global timeleft,x,timelbl
    timeleft = int(timeleft) - 1
    if (timeleft < 1):
        timelbl.destroy()
    timelbl.config(text ="Time Left: " + str(timeleft))
    Start()

def Start(*args):
    timelbl.after(1000, countdown)
    win.bind("<Return>", SentenceShuffle)

def SentenceShuffle(*args):
    global x,text,ransent,sentlbl,sentences
    text = txt.get()
    if text == ransent:
        x = x + 1
        pointslbl.config(text = "Score:" + str(x))
    ransent = random.choice(sentences)
    txt.delete(0, 'end')
    sentlbl.config(text = str(ransent))

win.bind("<0>", Start)

win.mainloop()