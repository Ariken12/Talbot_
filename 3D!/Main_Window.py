import tkinter as tk
import Front_Image as fi
import Side_Image as si


class Window(tk.Tk):

    def __init__(self):
        self.tk.Tk.__init__()
        self.FrontImage = fi.FrontImage()
        self.SideImage = si.SideImage()
        self._pack()

    def _pack(self):
