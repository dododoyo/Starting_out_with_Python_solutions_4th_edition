# ------- >>> Answer to multiple choice questions <<< ------- #

# 1,B   6,C   11,A  16,B 
# 2,A   7,A   12,D  17,D  
# 3,D   8,B   13,A  
# 4,C   9,D   14,C  
# 5,B   10,A  15,A  


# ------- >>> Answer to True or False questions <<< ------- #

# 1,False
# 2,False
# 3,False
# 4,True
# 5,False


# ------- >>> Answer to Short answer questions < ------- #

# 1
# When a program works on a text based environment the program determines the order in which things happen.

# 2
# The function of the pack method is to determine where the widget will be placed in its frame and makes
# the widget visibel when the main window is displayed. 

# 3
# The tkinter mainloop function runs like an infinte loop until the main window is closed. 

# 4
# If we don't specify an argument to the widget's pack method multiple widgets will show themselves stacked 
# on top of one another.

# 5
# To position a widget as far left as possible we pass side = 'left' argument into pack method.

# 6
# We can use entry's get method to retreive data that has been entered to the Entry widget.

# 7
# First we create some StringVar object then we associate that object with the lable that displays
# our output, after this any value that is stored in object will be displayed with the lable.

# 8
# We do this by associating each radio button with one IntVar object until one is selected, but after
# the radio button is selected the IntVar object will only be linked to the selected radio button.

# 9
# When working with CheckButtons we associate each checkbutton with different IntVar object 
# Then for each of the IntVar object we specify a task, so when called program will run it. 

# ------- >>> Answer to Algorithm Workbench Questions < ------- #
# 1
import tkinter
class Workbench1:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.Label1 = tkinter.Label(self.main_window, text = 'Programming is fun! ')
        self.Label1.pack()
        tkinter.mainloop()

# 2
import tkinter
class Workbench2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.Label1 = tkinter.Label(self.main_window,text = 'widget 1')
        self.Label2 = tkinter.Label(self.main_window, text = 'widget 2')
        self.Label1.pack(side = 'left')
        self.Label2.pack(side = 'left')

# 3
import tkinter
class Workbench3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.Frame1 = tkinter.Frame(self.main_window)
        self.Frame1.pack()
        tkinter.mainloop()

# 4
import tkinter
import tkinter.messagebox
class Workbench4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.Frame1 = tkinter.Frame(self.main_window)
        self.Frame1.pack()
        tkinter.mainloop()

# 5
import tkinter
class Workbench5:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.button_frame = tkinter.Frame(self.main_window)
        self.button1 = tkiner.Button(self.Frame1,text = 'Calculate',command = self.calculate)
        self.Frame1.pack()
        self.button1.pack()
        tkinter.mainloop()

# 6
import tkinter
class Workbench6:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.button_frame = tkinter.Frame(self.main_window)
        self.button1 = tkiner.Button(self.Frame1,text = 'Quit',command = self.quit)
        self.button_frame.pack()
        self.button1.pack()
        tkinter.mainloop()

# 7
import tkinter
class Workbench7:
    def __init__(self):
        self.main_window = tkinter.Tk() 
        self.entry_frame = tkinter(self.main_window) 
        self.entry = tkinter.Entry(self.entry_frame, width = 10) 
        self.var = int(self.entry.get()) 
        self.entry.pack()
        self.entry_frame.pack()
        tkinter.mainloop()
# 8
# (a)
import tkinter
class Workbench8a:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        self.canvas.create_line(0, 0, 199, 199,width = 3,fill = 'blue')
        self.canvas.pack()
        tkinter.mainloop()

# (b)
import tkinter
class Workbench8b:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        self.canvas.create_rectangle(50, 50, 100, 100,width = 3,fill = 'black', outline = 'red')
        self.canvas.pack()
        tkinter.mainloop()

# (c)
import tkinter
class Workbench8c:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        self.canvas.oval(50, 50, 150, 150)
        self.canvas.pack()
        tkinter.mainloop()

# (d)
import tkinter
class Workbench8d:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        self.canvas.create_arc(20, 20, 180, 180, start = 0, extent = 90, fill = 'blue')
        self.canvas.pack()
        tkinter.mainloop()
        