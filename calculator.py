from tkinter import *
import tkinter as tk

class cal:
    def __init__(self,master):
        self.master=master
        self.screen=Text(master,width=40,height=5,background="grey")
        self.screen.grid(row=0,column=0,columnspan=4)
        self.exp=''
        b1=Button(master,text="1",height=2,width=10,command=lambda:self.on_click(1)).grid(row=1,column=0)
        b2=Button(master,text="2",height=2,width=10,command=lambda:self.on_click(2)).grid(row=1,column=1)
        b3=Button(master,text="3",height=2,width=10,command=lambda:self.on_click(3)).grid(row=1,column=2)
        b4=Button(master,text="4",height=2,width=10,command=lambda:self.on_click(4)).grid(row=2,column=0)
        b5=Button(master,text="5",height=2,width=10,command=lambda:self.on_click(5)).grid(row=2,column=1)
        b6=Button(master,text="6",height=2,width=10,command=lambda:self.on_click(6)).grid(row=2,column=2)
        b7=Button(master,text="7",height=2,width=10,command=lambda:self.on_click(7)).grid(row=3,column=0)
        b8=Button(master,text="8",height=2,width=10,command=lambda:self.on_click(8)).grid(row=3,column=1)
        b9=Button(master,text="9",height=2,width=10,command=lambda:self.on_click(9)).grid(row=3,column=2)
        ba=Button(master,text="+",height=2,width=10,command=lambda:self.on_click("+")).grid(row=1,column=3)
        bs=Button(master,text="-",height=2,width=10,command=lambda:self.on_click("-")).grid(row=2,column=3)
        bm=Button(master,text="*",height=2,width=10,command=lambda:self.on_click("*")).grid(row=3,column=3)
        bd=Button(master,text="/",height=2,width=10,command=lambda:self.on_click("/")).grid(row=4,column=3)
        bc=Button(master,text="Clear screen",height=2,width=10,command=lambda:self.on_click("c")).grid(row=4,column=2)
        be=Button(master,text="=",height=2,width=22,command=lambda:self.on_click("=")).grid(row=4,column=0,columnspan=2)

    def on_click(self,t):
        if t=="=":
            answer=str(eval(self.exp))
            self.screen.delete(1.0,END)
            self.screen.insert(END,answer)
        elif t=="c":
            self.exp=''
            self.screen.delete(1.0,END)
        else:
            self.exp+=str(t)
            self.screen.insert(END,t)

start_engine=Tk()
Calculator=cal(start_engine)
start_engine.mainloop()
