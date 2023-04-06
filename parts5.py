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
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        self.canvas = tk.Canvas(self,width=173,height=200)
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

        self.w = master #把master傳給self.w這樣下面的def radioEvent(self)才可以使用master
        #因為main5.py裡的midFrame =MidFrame(self,borderwidth=0),Window(tk.Tk)就是這裡的master
        
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('clam')   

        # create ttk.radiobuttons in self
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT, padx=10, pady=10)

        self.radioStringVar = tk.StringVar()

        self.radiobutton1 = ttk.Radiobutton(radionFrame, text='Option 1', variable=self.radioStringVar, value ="1",command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(radionFrame, text='OOOOO', variable=self.radioStringVar, value ="2",command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(radionFrame, text='Option 3', variable=self.radioStringVar, value ="3",command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(radionFrame, text='Option 4', variable=self.radioStringVar, value ="4",command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set("3")

# create ttk.checkbuttons in self
        checkFrames = ttk.LabelFrame(self, text='Check Buttons')
        checkFrames.pack(side=tk.RIGHT, padx=10, pady=10)

        self.checkStringVar1 = tk.StringVar()
        self.checkStringVar2 = tk.StringVar()
        self.checkStringVar3 = tk.StringVar()
        self.checkStringVar4 = tk.StringVar()

        self.checkbutton1 = ttk.Checkbutton(checkFrames, text='Option 1',variable=self.checkStringVar1,command=self.checkEvent,onvalue="op1",offvalue="NOop1")
        self.checkbutton1.pack()
        self.checkbutton2 = ttk.Checkbutton(checkFrames, text='Option 2',variable=self.checkStringVar2,command=self.checkEvent,onvalue="op2",offvalue="NOop2")
        self.checkbutton2.pack()
        self.checkbutton3 = ttk.Checkbutton(checkFrames, text='Option 3', variable=self.checkStringVar3,command=self.checkEvent,onvalue="op3",offvalue="NOop3")
        self.checkbutton3.pack()
        self.checkbutton4 = ttk.Checkbutton(checkFrames, text='Option 4', variable=self.checkStringVar4,command=self.checkEvent,onvalue="op4",offvalue="NOop4")
        self.checkbutton4.pack()

    def radioEvent(self):
        self.w.radioButtonEventOfMidFrame(self.radioStringVar.get())

    def checkEvent(self):
        print(self.checkStringVar1.get())
        print(self.checkStringVar2.get())
        print(self.checkStringVar3.get())
        print(self.checkStringVar4.get())

