from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtGui


class Paint(Frame):

    def __init__(self, parent):
        
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()
        
    def set_color(self, new_color): 
    
        self.color = new_color 
    
    def set_brush_size(self, new_size): 
    
        self.brush_size = new_size 
    
    def draw(self, event): 
    
        self.canv.create_oval(event.x - self.brush_size, 
                              event.y - self.brush_size, 
                              event.x + self.brush_size, 
                              event.y + self.brush_size, 
                              fill=self.color, outline=self.color)     
    def setUI(self):

        self.parent.title("NedoPaint")  
        self.pack(fill=BOTH, expand=1)  
        self.columnconfigure(6, weight=1) 
        self.rowconfigure(2, weight=1)
        self.canv = Canvas(self, bg="white")  
        self.canv.grid(row=2, column=0, columnspan=7,
                      padx=5, pady=5, sticky=E+W+S+N) 
        self.canv.bind("<B1-Motion>", self.draw) 
        color_lab = Label(self, text="Color: ") 
        color_lab.grid(row=0, column=0, padx=6)
        red_btn = Button(self, bg="Red", width=10,
                         command=lambda: self.set_color("red")) 
        red_btn.grid(row=0, column=1) 
        green_btn = Button(self, bg="Green", width=10,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)
        blue_btn = Button(self, bg="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)
        black_btn = Button(self, bg="#555", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)
        white_btn = Button(self, bg="White", width=10,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)
        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)    