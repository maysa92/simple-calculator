import tkinter as tk
import tkinter.font as tkfont
import math
from PIL import ImageTk

class Calculator(tk.Frame):
    shouldReset = True #the flag
    self.imagesqrt = ImageTk.PhotoImage(file = "./SquareRoot.png")
    
    
    def _init_(self):
        tk.Frame._init_(self) #execute parent's constructor
        self.grid() #produce grids in the frame
        self.createWidgets()
    def createWidgets(self):
        f1 = tkfont.Font(size = 48, family = "Courier New")
        f2 = tkfont.Font(size = 32, family = "Courier New")
        self.lb1num = tk.Label(self, text = "0", height = 1, width = 9, font = f1)
        
        self.btn1 = tk.Button(self, text = "1", command = self.clickbtn1, height = 1, width = 2, font = f2)
        self.btn2 = tk.Button(self, text = "2", command = self.clickbtn2, height = 1, width = 2, font = f2)
        self.btn3 = tk.Button(self, text = "3", command = self.clickbtn3, height = 1, width = 2, font = f2)
        self.btn4 = tk.Button(self, text = "4", command = self.clickbtn4, height = 1, width = 2, font = f2)
        self.btn5 = tk.Button(self, text = "5", command = self.clickbtn5, height = 1, width = 2, font = f2)
        self.btn6 = tk.Button(self, text = "6", command = self.clickbtn6, height = 1, width = 2, font = f2)
        self.btn7 = tk.Button(self, text = "7", command = self.clickbtn7, height = 1, width = 2, font = f2)
        self.btn8 = tk.Button(self, text = "8", command = self.clickbtn8, height = 1, width = 2, font = f2)
        self.btn9 = tk.Button(self, text = "9", command = self.clickbtn9, height = 1, width = 2, font = f2)
        self.btn0 = tk.Button(self, text = "0", command = self.clickbtn0, height = 1, width = 2, font = f2)
        self.btnsqrt = tk.Button(self, image = self.imagesqrt, command = self.clickbtnsqrt, height = 1, width = 2, font = f2)
        
        self.lb1num.grid(row = 0, column = 0, columnspan = 3, sticky = tk.NE + tk.SW)
        self.btn1.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.btn2.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.btn3.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.btn4.grid(row = 2, column = 0, sticky = tk.NE + tk.SW)
        self.btn5.grid(row = 2, column = 1, sticky = tk.NE + tk.SW)
        self.btn6.grid(row = 2, column = 2, sticky = tk.NE + tk.SW)
        self.btn7.grid(row = 3, column = 0, sticky = tk.NE + tk.SW)
        self.btn8.grid(row = 3, column = 1, sticky = tk.NE + tk.SW)
        self.btn9.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)
        self.btn0.grid(row = 4, column = 0, columspan = 2, sticky = tk.NE + tk.SW)
        self.btnsqrt.grid(row = 4, column = 2, sticky = tk.NE + tk.SW)
        
    def setnumstr(self, content):
        if self.shouldReset == True:
            self.lb1num.configure(text = content)
            self.shouldReset = False
        else:
            self.lb1num.configure(text = self.lb1num.cget("text") + content)
    
    
    def clickbtn1(self):
        self.setnumstr("1")
    def clickbtn2(self):
        self.setnumstr("2")
    def clickbtn3(self):
        self.setnumstr("3")
    def clickbtn4(self):
        self.setnumstr("4")
    def clickbtn5(self):
        self.setnumstr("5")
    def clickbtn6(self):
        self.setnumstr("6")
    def clickbtn7(self):
        self.setnumstr("7")
    def clickbtn8(self):
        self.setnumstr("8")
    def clickbtn9(self):
        self.setnumstr("9")
    def clickbtn0(self):
        self.setnumstr("9")
    def clickbtnsqrt(self):
        curnum = float(self.lb1num.cget("text"))
        self.lb1num.configure(text = str(round(math.sqrt(curnum), 2)))
        self.shouldReset = True

    
cal = Calculator()
cal.master.title("My Calculator")
cal.mainloop() #to show up the frame and listen to events


#Adding widgets


