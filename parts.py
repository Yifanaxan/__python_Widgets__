import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TopFrame(ttk.LabelFrame):
    def __init__(self, master,**kwargs): #master是因為ttk.LabelFrame要求要寫
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
        #self.canvas = tk.Canvas(self,width=173,height=200)
        #self.canvas.pack()
        self.canvas.create_image(175,5,anchor='nw',image=self.diamondPhoto1)
        #self.canvas.create_text(0,200,anchor='sw',text="Diamond",fill='skyblue',font=('verdana',24))

        atomImage1 = Image.open("./images/atom.png")
        self.atomPhoto1 = ImageTk.PhotoImage(atomImage1)
        self.canvas.create_image(280,5,anchor='nw',image=self.atomPhoto1)

#created ttk.scrollbar of tkinter in canvas
        self.scrollbar = ttk.Scrollbar(self,orient="horizontal",command=self.canvas.xview) #The command parameter specifies that the scrollbar should control the x-view of the canvas widget self.canvas.
        self.scrollbar.pack(side='bottom',fill='x')
        self.canvas.configure(xscrollcommand=self.scrollbar.set,scrollregion=(0,00,500,200))
        #The first two values (0,0) specify the top-left corner of the scrollable area, and the last two values (500,200) specify the width and height of the area, respectively.


class MidFrame(ttk.LabelFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        # create ttk.radiobuttons in self
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT, padx=10, pady=10)
        self.radioStringvar = tk.StringVar()
        self.radiobutton1 = ttk.Radiobutton(radionFrame, text='Option 1', variable=self.radioStringvar, value ="red")
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(radionFrame, text='OOOOO', variable=self.radioStringvar, value ="vlue")
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(radionFrame, text='Option 3', variable=self.radioStringvar, value ="green")
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(radionFrame, text='Option 4', variable=self.radioStringvar, value ="yellow")
        self.radiobutton4.pack()
        self.radioStringvar.set("green")

# The variable parameter of each Radiobutton is set to radioStringvar, so that four buttons update the same variable. The value parameter of each button is set to a different value, which represents the choice of the button.

#When the user selects one of the buttons, the value of radioStringvar is automatically updated to the corresponding value. 