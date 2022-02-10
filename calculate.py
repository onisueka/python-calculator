from decimal import Decimal
import tkinter as tk
from tkinter import SUNKEN, Button, Label

gui = tk.Tk(className='Calculator')

# set window size
gui.geometry("190x240")

# button class
class Calculator:
    def __init__(self):
        self.first_nums = 0
        self.second_nums = 0
        self.display_nums = 0
        self.operate = ''
        self.historyType = ''
        self.setHeader()
        self.setBody([['7', 'number'], ['8', 'number'], ['9', 'number'], ['/', 'divide']])
        self.setBody([['4', 'number'], ['5', 'number'], ['6', 'number'], ['*', 'multiply']])
        self.setBody([['1', 'number'], ['2', 'number'], ['3', 'number'], ['-', 'minus']])
        self.setBody([['0', 'number'], ['.', 'decimal'], ['=', 'equal'], ['+', 'plus']])
    def doCalculate(self, object):
        if(self.historyType == 'error'): return
        if(self.operate == ''):
            if(object[1] == 'decimal' and str(self.first_nums).find('.') == 1): return
            match object[1]:
                case 'number' | 'decimal':
                    self.display_nums = self.first_nums = object[0] if self.first_nums == 0 and object[0] != 0 and object[0] != '.' else str(self.first_nums) + object[0]
                case 'plus' | 'minus' | 'multiply' | 'divide':
                    self.display_nums = self.first_nums
                    self.operate = object[1]
        else:
            if((self.historyType == 'number' or  self.historyType == 'decimal') and object[1] == 'decimal' and str(self.second_nums).find('.') == 1): return
            match object[1]:
                case 'number' | 'decimal':
                    if(self.historyType != 'number' and self.historyType != 'decimal'): self.second_nums = 0
                    self.display_nums = self.second_nums = object[0] if self.second_nums == 0 and object[0] != 0 and object[0] != '.' else str(self.second_nums) + object[0]
                case 'plus' | 'minus' | 'multiply' | 'divide' | 'equal':
                    if((self.historyType == 'number' or object[1] == 'equal') and (self.operate == object[1] or object[1] == 'equal')):
                        match self.operate:
                            case 'plus':
                                self.first_nums = Decimal(self.first_nums) + Decimal(self.second_nums)
                            case 'minus':
                                self.first_nums = Decimal(self.first_nums) - Decimal(self.second_nums)
                            case 'multiply':
                                self.first_nums = Decimal(self.first_nums) * Decimal(self.second_nums)
                            case 'divide':
                                if(Decimal(self.second_nums) == 0):
                                    self.display.config(text='Cannot divide!')
                                    self.historyType = 'error'
                                    self.doClear()
                                    return
                                else:
                                    self.first_nums = Decimal(self.first_nums) / Decimal(self.second_nums)   

                        self.display_nums = self.first_nums = str(Decimal(self.first_nums))

                    if(object[1] != 'equal'): self.second_nums = self.first_nums
                    self.operate = object[1] if object[1] != 'equal' else self.operate
        self.historyType = object[1]
        self.display.config(text=self.display_nums)
    def doClear(self, type=None):
        self.first_nums = 0
        self.second_nums = 0
        self.operate = ''
        if(type != None):
            self.display_nums = 0
            self.display.config(text=self.display_nums)
            self.historyType = ''
    def setHeader(self):
        pack_frame = tk.Frame(gui)
        pack_frame.pack()
        self.display = Label(pack_frame, text=self.display_nums, height=2, width=12, relief=SUNKEN, background='black', foreground='white', anchor='e', padx=10) 
        self.display.pack(side=tk.LEFT,fill=tk.X, expand=True, padx=4)
        clear_button = Button(pack_frame, text='c', background='#D1354A', height=2, width=2, command=lambda: self.doClear('all'))
        clear_button.bind("<Leave>", func=lambda e: clear_button.config(background = '#D1354A'))
        clear_button.bind("<Enter>", func=lambda e: clear_button.config(activebackground = '#D5495C'))
        clear_button.pack(side=tk.LEFT,fill=tk.X, expand=True) 
    def setBody(self, frameArray):
        pack_frame = tk.Frame(gui)
        pack_frame.pack()
        for frame in frameArray:
            Button(pack_frame, text=frame[0], height=2, width=2, command=lambda frame=frame: self.doCalculate(frame)).pack(side=tk.LEFT,fill=tk.X, expand=True) 

# create calculator
calculator = Calculator()

# start the GUI 
gui.mainloop()