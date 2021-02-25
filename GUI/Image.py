from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Button
from tkinter.ttk import Frame, Label
import sys


class ImagePanel(Frame):
    def __init__(self, **args):
        super().__init__(**args)
        self.width, self.height = 500, 500
        self.img = Image
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.button_right = Button(self, text='Вправо', command=self.__move_right)
        self.button_left = Button(self, text='Влево', command=self.__move_left)
        self.button_up = Button(self, text='Вверх', command=self.__move_up)
        self.button_down = Button(self, text='Вниз', command=self.__move_down)
        
    def load_image(self, image_name):
        try:
            self.img = Image.open(image_name)
        except IOError:
            raise IOError

    def upload_img(self):
        self.tatras = ImageTk.PhotoImage(self.img)
        width, height = self.img.size
        print(width, height)
        self.x, self.y = 0, 0
        self.speed_x, self.speed_y = self.width/5, self.height/5
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='white', outline='white')
        self.description = Label(self, text='Превью')
        self.canvas.image = self.tatras
        self.__draw_image()
        self.__pack()

    def __draw_image(self):
        self.image = self.canvas.create_image(self.x, self.y, image=self.tatras)
        self.canvas.update()
    
    def __move_right(self):
        self.canvas.delete(self.image)
        self.x -= self.speed_x
        self.__draw_image()

    def __move_left(self):
        self.canvas.delete(self.image)
        self.x += self.speed_x
        self.__draw_image()

    def __move_up(self):
        self.canvas.delete(self.image)
        self.y += self.speed_y
        self.__draw_image()

    def __move_down(self):
        self.canvas.delete(self.image)
        self.y -= self.speed_y
        self.__draw_image()

    def __pack(self):
        self.description.grid(row=1, column=1, columnspan=3)
        self.canvas.grid(row=2, column=1, columnspan=3)
        self.button_left.grid(row=3, column=1, rowspan=2)
        self.button_right.grid(row=3, column=3, rowspan=2)
        self.button_up.grid(row=3, column=2)
        self.button_down.grid(row=4, column=2)