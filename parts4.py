import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TopFrame(ttk.LabelFrame):
    def __init__(self, master,**kwargs): 
        super().__init__(master, **kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('TLabelframe',borderwidth=0)
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)#self.就是一個attrubute
        self.canvas = tk.Canvas(self,width=173,height=200)#self原本是寫topFrame
        self.canvas.pack()
        self.canvas.create_image(0,5,anchor='nw',image=self.flowerPhoto1)
        self.canvas.create_text(0,200,anchor='sw',text="Flower",fill='skyblue',font=('verdana',24))

        diamondImage1 = Image.open("./images/diamond.png")
        self.diamondPhoto1 = ImageTk.PhotoImage(diamondImage1)
        self.canvas.create_image(175,5,anchor='nw',image=self.diamondPhoto1)

        atomImage1 = Image.open("./images/atom.png")
        self.atomPhoto1 = ImageTk.PhotoImage(atomImage1)
        self.canvas.create_image(280,5,anchor='nw',image=self.atomPhoto1)

#created ttk.scrollbar of tkinter in canvas
        self.scrollbar = ttk.Scrollbar(self,orient="horizontal",command=self.canvas.xview) 
        self.scrollbar.pack(side='bottom',fill='x')
        self.canvas.configure(xscrollcommand=self.scrollbar.set,scrollregion=(0,00,500,200))

class MidFrame(ttk.LabelFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        # create ttk.radiobuttons in self
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT, padx=10, pady=10)
        self.radioStringVar = tk.StringVar()
        self.radiobutton1 = ttk.Radiobutton(radionFrame, text='Option 1', variable=self.radioStringVar, value ="1",command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(radionFrame, text='OOOOO', variable=self.radioStringVar, value ="3",command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(radionFrame, text='Option 3', variable=self.radioStringVar, value ="3",command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(radionFrame, text='Option 4', variable=self.radioStringVar, value ="4",command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set("3")
        #the value of the StringVar named self.radioStringVar is being set to "3". This means that if there are any Radiobuttons associated with this StringVar, the radio button with the value of "3" will be selected.

    def radioEvent(self):
        print(self.radioStringVar.get())
