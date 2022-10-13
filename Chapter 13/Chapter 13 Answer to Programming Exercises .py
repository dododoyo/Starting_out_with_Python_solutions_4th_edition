#   ------- >>> Answer to Programming Exercises <<< ------- #

# 1
import tkinter
class name_and_address:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.upper = tkinter.Frame(self.main_window)
        self.lower = tkinter.Frame(self.main_window)
        self.the_object = tkinter.StringVar()
        self.show_message = tkinter.Label(self.upper, textvariable = self.the_object)
        self.showinfobutton = tkinter.Button(self.lower,text = 'Show Info',command = self.information)
        self.quitbutton = tkinter.Button(self.lower,text = 'Quit', command = self.main_window.destroy)
        
        self.showinfobutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')
        self.show_message.pack()
        self.upper.pack()
        self.lower.pack()
        tkinter.mainloop()

    def information(self):
        the_string = 'Dolphin Mulugeta\nAddis Ababa, Ethiopia\nBole street 42322'
        self.the_object.set(the_string)

# 2
import tkinter
class Translator:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.upper_frame = tkinter.Frame(self.main_window)
        self.middle1_frame = tkinter.Frame(self.main_window)
        self.middle2_frame = tkinter.Frame(self.main_window)
        self.lower_frame = tkinter.Frame(self.main_window)
        self.chb1 = tkinter.StringVar()
        self.chb2 = tkinter.StringVar()
        self.chb3 = tkinter.StringVar()
    
        self.topper = tkinter.Label(self.upper_frame, text = 'Latin         |      English')
        self.button1 = tkinter.Button(self.middle1_frame, text = 'sinister', command = self.show1)
        self.button2 = tkinter.Button(self.middle2_frame, text = 'dexter', command = self.show2)
        self.button3 = tkinter.Button(self.lower_frame, text = 'medium', command = self.show3)
        self.label1 = tkinter.Label(self.middle1_frame,textvariable = self.chb1)
        self.label2 = tkinter.Label(self.middle2_frame,textvariable = self.chb2)
        self.label3 = tkinter.Label(self.lower_frame,textvariable = self.chb3)
        
        self.topper.pack()
        self.upper_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.lower_frame.pack()
        self.button1.pack(side = 'left')
        self.button2.pack(side = 'left')
        self.button3.pack(side = 'left')
        self.label1.pack(side = 'right')
        self.label2.pack(side = 'right')
        self.label3.pack(side = 'right')
        tkinter.mainloop()

    def show1(self):
        self.chb1.set('left')
    def show2(self):
        self.chb2.set('right')
    def show3(self):
        self.chb3.set('center')
        
# 3
import tkinter
class Show_mile:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.upper_frame = tkinter.Frame(self.main_window)
        self.upper2frame = tkinter.Frame(self.main_window)
        self.lower_frame2 = tkinter.Frame(self.main_window)
        self.lower_frame = tkinter.Frame(self.main_window)
        self.MPG_value = tkinter.StringVar()
        self.label1 = tkinter.Label(self.upper_frame, text = 'Please enter the number of gallons of gas the car holds.')
        self.label2 = tkinter.Label(self.upper2frame, text = 'Please enter the number of miles driven on a full tank.')
        self.gallons = tkinter.Entry(self.upper_frame, width = 10)
        self.miles = tkinter.Entry(self.upper2frame, width = 10)
        self.label3 = tkinter.Label(self.lower_frame2, text = 'The car\'s MPG is :')
        self.MPg_shower = tkinter.Label(self.lower_frame2,textvariable = self.MPG_value)
        self.convert_button = tkinter.Button(self.lower_frame, text = 'Display', command = self.calculator)
        self.quitbutton = tkinter.Button(self.lower_frame, text = 'Quit', command = self.main_window.destroy)
        
        self.upper_frame.pack()
        self.upper2frame.pack()
        self.lower_frame2.pack()
        self.lower_frame.pack()
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')
        self.miles.pack(side = 'left')
        self.gallons.pack(side = 'left')
        self.MPg_shower.pack(side = 'left')
        self.convert_button.pack(side = 'left')
        self.quitbutton.pack(side = 'left')
        tkinter.mainloop()

    def calculator(self):
        mpg = int(self.miles.get())/int(self.gallons.get())
        mpg = format(mpg,',.2f')
        self.MPG_value.set(mpg)

# 4
import tkinter
class to_fahrenheit:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.fahreniet_value = tkinter.StringVar()
        self.label1 = tkinter.Label(self.frame1, text = 'Please enter temprature value in celsius: ')    
        self.selsius = tkinter.Entry(self.frame2, width = 10)
        self.fahrenheit_shower = tkinter.Label(self.frame2,textvariable = self.fahreniet_value)
        self.convert_button = tkinter.Button(self.frame3, text = 'Display', command = self.calculator)
        self.quitbutton = tkinter.Button(self.frame3, text = 'Quit', command = self.main_window.destroy)
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.label1.pack()
        self.selsius.pack(side = 'left')
        self.fahrenheit_shower.pack(side = 'left')
        self.convert_button.pack(side = 'left')
        self.quitbutton.pack(side = 'left')
        tkinter.mainloop()

    def calculator(self):
        fahren = (int(self.selsius.get())*9)/5 + 32
        fahren = format(fahren, ',.2f')
        self.fahreniet_value.set(fahren)

# 5
import tkinter
class property_tax:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.ass_value = tkinter.StringVar()
        self.tax_value = tkinter.StringVar()
        self.label1 = tkinter.Label(self.frame1,text = 'Please enter actual value of the property: ')
        self.the_entry = tkinter.Entry(self.frame1,width=12)
        self.label2 = tkinter.Label(self.frame2, text = 'The assesment value of the property is: ')
        self.label3 = tkinter.Label(self.frame2,textvariable= self.ass_value)
        self.label4 = tkinter.Label(self.frame3, text = 'The tax for the property will be: ')
        self.label5 = tkinter.Label(self.frame3, textvariable=self.tax_value)
        self.button1 = tkinter.Button(self.frame4, text = 'Show Values', command = self.tax_shower)
        self.button2 = tkinter.Button(self.frame4, text = 'Quit', command = self.main_window.destroy)
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.label1.pack(side = 'left')
        self.the_entry.pack(side = 'left')
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')
        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.button1.pack(side = 'left')
        self.button2.pack(side = 'left')
        tkinter.mainloop()

    def tax_shower(self):
        actual_value = int(self.the_entry.get())
        assesment = actual_value*0.6
        tax_ = assesment*0.0075
        assesment = format(assesment, ',.2f')
        tax_ = format(tax_, ',.2f')
        self.ass_value.set(assesment)
        self.tax_value.set(tax_)

# 6
import tkinter
class joe_automotive:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.value1 = tkinter.IntVar()
        self.value2 = tkinter.IntVar()
        self.value3 = tkinter.IntVar()
        self.value4 = tkinter.IntVar()
        self.value5 = tkinter.IntVar()
        self.value6 = tkinter.IntVar()
        self.value7 = tkinter.IntVar()
        self.value1.set(0)
        self.value2.set(0)
        self.value3.set(0)
        self.value4.set(0)
        self.value5.set(0)
        self.value6.set(0)
        self.value7.set(0)
        self.total = tkinter.StringVar()
        self.label1 = tkinter.Label(self.frame1,text = 'Please select desired maintainance services: ')
        self.chb1 = tkinter.Checkbutton(self.frame2, text = 'Oil change', variable = self.value1)
        self.chb2 = tkinter.Checkbutton(self.frame2, text = 'Lube job', variable = self.value2)
        self.chb3 = tkinter.Checkbutton(self.frame2, text = 'Radiator flush', variable = self.value3)
        self.chb4 = tkinter.Checkbutton(self.frame2, text = 'Transmission flush', variable = self.value4)
        self.chb5 = tkinter.Checkbutton(self.frame2, text = 'Inspection', variable = self.value5)
        self.chb6 = tkinter.Checkbutton(self.frame2, text = 'Muffler replacement', variable = self.value6)
        self.chb7 = tkinter.Checkbutton(self.frame2, text = 'Tire rotation', variable = self.value7)
        self.button1 = tkinter.Button(self.frame3, text = 'Show total', command = self.total_calculator)
        self.label3 = tkinter.Label(self.frame3, textvariable = self.total)
        self.button2 = tkinter.Button(self.frame4, text = 'Quit', command = self.main_window.destroy)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.label1.pack(side = 'left')
        self.button1.pack(side = 'left')
        self.label3.pack(side = 'right')
        self.chb1.pack()
        self.chb2.pack()
        self.chb3.pack()
        self.chb4.pack()
        self.chb5.pack()
        self.chb6.pack()
        self.chb7.pack()
       
        self.button2.pack(side = 'left')

        tkinter.mainloop()
    def total_calculator(self):
        total_cost = 0
        if self.value1.get() == 1:
            total_cost += 30
        if self.value2.get() == 1:
            total_cost += 20
        if self.value3.get() == 1:
            total_cost += 40
        if self.value4.get() == 1:
            total_cost += 100
        if self.value5.get() == 1:
            total_cost += 35
        if self.value6.get() == 1:
            total_cost += 200
        if self.value7.get() == 1:
            total_cost += 20
        self.total.set(total_cost)

# 7
import tkinter
class call_fee:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.total_value = tkinter.StringVar()
        self.label1 = tkinter.Label(self.frame1,text = 'Please enter number of minutes of the call: ')
        self.the_entry = tkinter.Entry(self.frame1,width=12)
        self.the_value = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.frame2,text = 'Daytime',variable=self.the_value, value = 1)
        self.rb2 = tkinter.Radiobutton(self.frame2,text = 'Evening',variable=self.the_value, value = 2)
        self.rb3 = tkinter.Radiobutton(self.frame2,text = 'Off-Peak',variable=self.the_value, value = 3)
        self.label2 = tkinter.Label(self.frame3, textvariable = self.total_value)
        self.button1 = tkinter.Button(self.frame3, text = 'Show Call Fee: ', command = self.call_shower)
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.label1.pack(side = 'left')
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.the_entry.pack(side = 'left')
        self.button1.pack(side = 'left')
        self.label2.pack(side = 'left')
        tkinter.mainloop()

    def call_shower(self):
        minutes = float(self.the_entry.get())
        if self.the_value.get() == 1:
            rate = 0.07
        elif self.the_value.get() == 2:
            rate = 0.12
        else:
            rate = 0.05
        total_call_fee = rate*minutes
        self.total_value.set(total_call_fee)

# 8
import tkinter
class old_canvas_house:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 300, height = 300)
        self.canvas.create_line(80,150,130,75,180,150)
        self.canvas.create_rectangle(80,150,180,250)
        self.canvas.create_rectangle(90,170,110,190)
        self.canvas.create_rectangle(150,170,170,190)
        self.canvas.create_rectangle(115,200,145,250)
        self.canvas.pack()
        tkinter.mainloop()

# 9
import tkinter
class tree_rings:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 250, height = 250)
        self.canvas.create_oval(105,105,145,145)
        self.canvas.create_oval(85,85,185,185)
        self.canvas.create_oval(65,65,205,205)
        self.canvas.create_oval(45,45,225,225)
        self.canvas.create_oval(25,25,245,245)
        self.canvas.create_text(123,125,text = 'Year 1')
        self.canvas.create_text(175,115,text = 'Year 2')
        self.canvas.create_text(70,140,text = 'Year 3')
        self.canvas.create_text(225,135,text = 'Year 4')
        self.canvas.create_text(20,105,text = 'Year 5')
        self.canvas.pack()
        tkinter.mainloop()
    
# 10
import tkinter
class hollywood_star:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 300, height = 300)
        self.canvas.create_line(50,70, 90,70 ,100,20 ,110,70 ,150,70 ,125,105 ,130,150 ,100,125 ,70,150 ,80,105 ,50,70)
        self.canvas.create_text(105, 95, text = 'Dolphin')
        self.canvas.pack()
        tkinter.mainloop()

# 11
import tkinter
class the_car:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 300, height = 300)
        self.canvas.create_line(65,180, 20,180, 20,140, 75,140 ,75,100 ,175,100 ,175,140 ,230,140 ,230,180, 185,180 )
        self.canvas.create_arc(65,170 ,85,190, start = 0, extent = 180, style =tkinter.ARC)
        self.canvas.create_line(85,180, 165,180)
        self.canvas.create_arc(165,170 ,185,190, start = 0, extent = 180, style =tkinter.ARC)
        self.canvas.create_oval(168,173, 182,187)
        self.canvas.create_oval(68,173, 82,187)
        
        self.canvas.pack()
        tkinter.mainloop()

# 12
import tkinter
class solar_system:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 400, height = 400)
        self.canvas.create_oval(5,5,395,395)
        self.canvas.create_oval(20,20,380,380)
        self.canvas.create_oval(40,40, 360,360)
        self.canvas.create_oval(60,60, 340,340)
        self.canvas.create_oval(80,80, 320,320)
        self.canvas.create_oval(100,100, 300,300)
        self.canvas.create_oval(120,120, 280,280)
        self.canvas.create_oval(140,140, 260,260)
        self.canvas.create_oval(160,160, 240,240)

        self.canvas.create_oval(190,190, 210,210, fill = 'yellow')
        self.canvas.create_text(185,185, text = 'SUN')

        self.canvas.create_oval(280,15, 295,30, fill = 'orange')
        self.canvas.create_text(290,10, text = 'Pluto')
    
        self.canvas.create_oval(185,35, 200,50, fill = 'black')
        self.canvas.create_text(170,35, text ='Saturn')

        self.canvas.create_oval(64,145, 79,160, fill = 'magenta')
        self.canvas.create_text(70,140,text = 'Uranus')

        self.canvas.create_oval(31,113, 45,127, fill = 'gray')
        self.canvas.create_text(35,105,text = 'Neptune')

        self.canvas.create_oval(117,117, 140,140, fill = 'brown')
        self.canvas.create_text(124,112,text = 'Jupiter')

        self.canvas.create_oval(265,220, 280,235, fill = 'green')
        self.canvas.create_text(280,215, text = "Mars",)

        self.canvas.create_oval(227,215, 242,230, fill='cyan')
        self.canvas.create_text(240,200, text = "Mercury",)

        self.canvas.create_oval(230,150, 245,165, fill = 'red')
        self.canvas.create_text(225,137,text = 'Venus' )

        self.canvas.create_text(175,115,text = 'Earth')
        self.canvas.create_oval(185,115, 200,130, fill = 'blue') 
        
        self.canvas.pack()
        tkinter.mainloop()