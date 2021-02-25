import tkinter as tk
from tkinter import messagebox as mb
from GUI import InputPanel as ip
from GUI import Image as img
from LinearWaves import talbot as talbot_main
import numpy as np


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Talbot')
        self.input_panel = ip.InputPanel()
        self.image = img.ImagePanel()
        self.computation_button = tk.Button(self, text="Расчитать", command=self.trigger_button)
        self.image.grid(row=1, column=1, rowspan=2)
        self.computation_button.grid(row=2, column=2)
        self.input_panel.grid(row=1, column=2)
        self.set_default()

    def set_default(self):
        self.input_panel.step_entry.insert(0, '0.5')
        self.input_panel.n_entry.insert(0, '1')
        self.input_panel.open_entry.insert(0, '1')
        self.input_panel.close_entry.insert(0, '500')

    def trigger_button(self):
        step = float(self.input_panel.step_entry.get())
        n = int(self.input_panel.n_entry.get())
        open_pixels = int(self.input_panel.open_entry.get())
        close_pixels = int(self.input_panel.close_entry.get())
        talbot_main.talbot(step=step, n=n, open=open_pixels, close=close_pixels)
        self.image.load_image("Talbot.png")
        self.image.upload_img()
        self.update()

