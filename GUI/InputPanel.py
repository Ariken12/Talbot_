import tkinter as tk


class InputPanel(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.step_label = tk.Label(self, text="Шаг тангенса")
        self.n_label = tk.Label(self, text="Количество лучей")
        self.open_label = tk.Label(self, text="Количество пикселей открытой части")
        self.close_label = tk.Label(self, text="Количестко пикселей закрытой части")
        self.step_entry = tk.Entry(self)
        self.n_entry = tk.Entry(self)
        self.open_entry = tk.Entry(self)
        self.close_entry = tk.Entry(self)
        self.__pack()

    def __pack(self):
        self.step_label.grid(row=1, column=1)
        self.step_entry.grid(row=1, column=2)
        self.n_label.grid(row=2, column=1)
        self.n_entry.grid(row=2, column=2)
        self.open_label.grid(row=3, column=1)
        self.open_entry.grid(row=3, column=2)
        self.close_label.grid(row=4, column=1)
        self.close_entry.grid(row=4, column=2)