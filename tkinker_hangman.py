import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from tkinter import *
  
window = tk.Tk() 
window.geometry('350x250') 
ttk.Label(window, text = "Select the Genre :",  
        font = ("Times New Roman", 10)).grid(column = 0,  
        row = 15, padx = 10, pady = 25) 
  
n = tk.StringVar() 
genrechoosen = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
genrechoosen['values'] = (' Comedy',
                          ' Sci-Fi',  
                          ' Horror', 
                          ' Romance', 
                          ' Action',
                          ' Thriller',    
                          ' Drama',
                          ' Mystery',  
                          ' Crime',    
                          ' Animation',
                          ' Adventure',  
                          ' Fantasy') 
genrechoosen.grid(column = 1, row = 15) 
if genrechoosen == 'Comedy':
        messagebox.showinfo("you have selected Comedy", "please wait while the data is been extracted")


genrechoosen.current(1)  
window.mainloop() 