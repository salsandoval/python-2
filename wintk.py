Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> 
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.pack()
>>> b2.pack()
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b1.pack(side = LEFT, padx = 10)
>>> b2.pack(side = LEFT, padx = 10)
>>> b3 = Button(win, text="Three")
>>> b4 = Button(win, text="Four")
>>> b3.pack()
>>> b4.pack()
>>> b3.pack(side=BOTTOM)
>>> b4.pack(side=TOP)
>>> b3.pack(side = LEFT, padx = 10)
>>> b4.pack(side = LEFT, padx = 10)
>>> b4.pack(side = RIGHT, padx = 10)
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.grid(row=0, column=0)
>>> b2.grid(row=1, column=1)
>>> 1 = Label(win, text="This is a label")
SyntaxError: cannot assign to literal
>>> l = Label(win, text="This is a label")
>>> l.grid(row=1, column=0)
>>> win = Tk()
>>> f = Frame(win)
>>> b1 = Button(f, text="One")
>>> b2 = Button(f, text="Two")
>>> b3 = Button(f, text="Three")
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b3.pack(side=LEFT)
>>> l = Label(win, text="This label is over all buttons")
>>> l.pack()
>>> f.pack()
>>> b1.configure(text="Uno")
>>> def but1():
	print("Button one was pushed")

	
>>> b1.configure(command=but1)
>>> Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
SyntaxError: invalid syntax
>>> win = Tk()
>>> v = StringVar()
>>> e = Entry(win, textvariable = v)
>>> e.pack()
>>> v.get()
''
>>> v.get()
''
>>> v.set("this is set by the program")
>>> v.set("this is set by the program")
>>> win = Tk()
>>> v = stringVar()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    v = stringVar()
NameError: name 'stringVar' is not defined
>>> v = StringVar()
>>> e = Entry(win, textvariable = v)
>>> e.pack()
>>> v.get()
''
>>> v.get()
''
>>> win = Tk()
>>> lb = Listbox(win, height=3)
>>> lb.pack()
>>> lb.insert(END, "first entry")
>>> lb.insert(END, "second entry")
>>> lb.insert(END, "fourth entry")
>>> lb.insert(END, "third entry")
>>> sb = Scrollbar(win, orient_VERTICAL)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    sb = Scrollbar(win, orient_VERTICAL)
NameError: name 'orient_VERTICAL' is not defined
>>> sb = Scrollbar(win, orient=VERTICAL)
>>> sb.pack(side=LEFT, fill=Y)
>>> sb.configure(command=lb.yview)
>>> lb.configure(yscrollcommand=sb.set)
>>> lb.curselection()
(2,)
>>> 