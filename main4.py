import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from parts4 import TopFrame, MidFrame

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        topFrame =TopFrame(self,borderwidth=0) 
        topFrame.pack()
        midFrame =MidFrame(self,borderwidth=0) 
        midFrame.pack(fill=tk.X)

    def radioButtonEventOfMidFrame(self,radioButtonValue):
        print(radioButtonValue)




def main():
    window = Window()
    window.title("Widgets") 
    window.mainloop()

if __name__ == "__main__":
    main()
