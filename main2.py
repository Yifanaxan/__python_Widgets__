import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from parts import TopFrame

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        topFrame =TopFrame(self,borderwidth=0) #borderwidth傳給TopFrame的**kwargs
        print(topFrame.flowerPhoto1)
        topFrame.pack()
'''
master是參數名稱
可以自行定義

Window是父容器
topFrame是子容器

LabelFrame是父類別
TopFrame是子類別
'''

def main():
    window = Window()
    window.title("Widgets")   #也可以在class Window裡面寫self.title
    window.mainloop()

if __name__ == "__main__":
    main()
