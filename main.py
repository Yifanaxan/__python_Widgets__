import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

'''
def DrawImageWithTkinter():
    root = tk.Tk()
    root.title("Drawing an Image")
    root.geometry("400x400")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    img = tk.PhotoImage(file="image.png")
    canvas.create_image(20, 20, anchor=tk.NW, image=img)
    root.mainloop()
'''
'''
class TopFrame(ttk.LabelFrame):
    def __init__(self, master: tkinter.Misc | None = None, *, border: tkinter._ScreenUnits = ..., borderwidth: tkinter._ScreenUnits = ..., class_: str = ..., cursor: tkinter._Cursor = ..., height: tkinter._ScreenUnits = ..., labelanchor: Literal["nw", "n", "ne", "en", "e", "es", "se", "s", "sw", "ws", "w", "wn"] = ..., labelwidget: tkinter.Misc = ..., name: str = ..., padding: _Padding = ..., relief: tkinter._Relief = ..., style: str = ..., takefocus: tkinter._TakeFocusValue = ..., text: float | str = ..., underline: int = ..., width: tkinter._ScreenUnits = ...) -> None:
        super().__init__(master, border=border, borderwidth, class_, cursor, height, labelanchor, labelwidget, name, padding, relief, style, takefocus, text, underline, width)
'''
class TopFrame(ttk.LabelFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self)
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        canvas = tk.Canvas(topFrame,width=173,height=200)
        canvas.pack()
        canvas.create_image(0,0,anchor='nw',image=self.flowerPhoto1)
        canvas.create_text(0,200,anchor='sw',text="Flower",fill='skyblue',font=('verdana',24))
        topFrame.pack()



def main():
    window = Window()
    window.title("Widgets")   #也可以在class Window裡面寫self.title
    window.mainloop()

if __name__ == "__main__":
    main()
