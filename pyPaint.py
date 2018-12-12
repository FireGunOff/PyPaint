from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtGui


class Paint(Frame):

    def __init__(self, parent):
        
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()