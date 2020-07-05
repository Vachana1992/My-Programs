import tkinter

class Calculator:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("My Calculator")
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.num_entry = tkinter.Entry(self.top_frame, width = 55 , borderwidth=5 )
        self.num_entry.grid(row= 0 , column = 0 , columnspan = 3, padx = 10, pady = 10)

        #Define button
        from _ast import Lambda
        self.button1 = tkinter.Button(self.bottom_frame, text='1', padx=40 ,pady=20, command=lambda:self.click(1))
        self.button2 = tkinter.Button(self.bottom_frame, text='2', padx=40, pady=20, command=lambda:self.click(2))
        self.button3 = tkinter.Button(self.bottom_frame, text='3', padx=40, pady=20, command=lambda:self.click(3))
        self.button4 = tkinter.Button(self.bottom_frame, text='4', padx=40, pady=20, command=lambda:self.click(4))
        self.button5 = tkinter.Button(self.bottom_frame, text='5', padx=40, pady=20, command=lambda:self.click(5))
        self.button6 = tkinter.Button(self.bottom_frame, text='6', padx=40, pady=20, command=lambda:self.click(6))
        self.button7 = tkinter.Button(self.bottom_frame, text='7', padx=40, pady=20, command=lambda:self.click(7))
        self.button8 = tkinter.Button(self.bottom_frame, text='8',padx = 40,pady=20 ,command=lambda:self.click(8))
        self.button9 = tkinter.Button(self.bottom_frame, text='9', padx=40, pady=20, command=lambda:self.click(9))
        self.button0 = tkinter.Button(self.bottom_frame, text='0', padx=40, pady=20, command=lambda:self.click(0))
        self.button_dot = tkinter.Button(self.bottom_frame, text='.', padx=40, pady=20, command=lambda:self.click("."))

        self.button_add = tkinter.Button(self.bottom_frame, text='+', padx=40, pady=20, command=self.add)
        self.button_sub = tkinter.Button(self.bottom_frame, text='-', padx=40, pady=20, command=self.sub)
        self.button_mul = tkinter.Button(self.bottom_frame, text='x', padx=40, pady=20, command=self.mul)
        self.button_div = tkinter.Button(self.bottom_frame, text='/', padx=40, pady=20, command=self.div)
        self.button_mod = tkinter.Button(self.bottom_frame, text='%', padx=40, pady=20, command=self.mod)

        self.button_equal = tkinter.Button(self.bottom_frame, text='=', padx=40, pady=20, command=self.equal)
        self.button_clear = tkinter.Button(self.bottom_frame, text='Clear', padx=30, pady=20, command=self.clear)

        #put the button on the screen

        self.button1.grid(row=3 , column =0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)

        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)

        self.button0.grid(row=4, column=0)
        self.button_add.grid(row= 4, column=2)
        self.button_equal.grid(row=5, column=2)
        self.button_clear.grid(row=6, column=2)
        self.button_sub.grid(row=4, column=1)
        self.button_mul.grid(row=5, column=0)
        self.button_div.grid(row=5, column=1)
        self.button_mod.grid(row=6, column=0)
        self.button_dot.grid(row=6, column=1)




        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def click(self,number):
        #self.num_entry.delete(0, tkinter.END)
        current = self.num_entry.get()
        self.num_entry.delete(0,tkinter.END)
        self.num_entry.insert(0,str(current)+str(number))

    def clear(self):
        self.num_entry.delete(0, tkinter.END)

    def add(self):
        self.first_number = self.num_entry.get()
        global f_num
        global  math
        math = "addition"
        self.f_num = int(self.first_number)
        self.num_entry.delete(0,tkinter.END)

    def sub(self):
        self.first_number = self.num_entry.get()
        global f_num
        global math
        math = "subtraction"
        self.f_num = int(self.first_number)
        self.num_entry.delete(0, tkinter.END)

    def mul(self):
        self.first_number = self.num_entry.get()
        global f_num
        global math
        math = "multiplication"
        self.f_num = int(self.first_number)
        self.num_entry.delete(0, tkinter.END)

    def div(self):
        self.first_number = self.num_entry.get()
        global f_num
        global math
        math = "division"
        self.f_num = int(self.first_number)
        self.num_entry.delete(0, tkinter.END)

    def mod(self):
        self.first_number = self.num_entry.get()
        global f_num
        global math
        math = "modulus"
        self.f_num = int(self.first_number)
        self.num_entry.delete(0, tkinter.END)

    def equal(self):
        self.second_number = self.num_entry.get()
        self.num_entry.delete(0,tkinter.END)

        if math == "addition":
            self.num_entry.insert(0,self.f_num + int(self.second_number))

        if math == "subtraction":
            self.num_entry.insert(0,self.f_num - int(self.second_number))

        if math == "multiplication":
            self.num_entry.insert(0,self.f_num * int(self.second_number))

        if math == "division":
            self.num_entry.insert(0,self.f_num / int(self.second_number))

        if math == "modulus":
            self.num_entry.insert(0,self.f_num % int(self.second_number))

calc = Calculator()