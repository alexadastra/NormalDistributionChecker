from tkinter import *
from tkinter import filedialog
import main as algorithm
import matplotlib as plt
from PIL import ImageTk, Image
import os
import sys


class EquationParamsWidget(object):
    def __init__(self, fields, master):
        indices = []
        for i in range(len(fields)):
            indices.append(i)
        self.collection = dict.fromkeys(indices)
        for counter in range(0, len(fields)):
            if not counter % 2:
                color = "#0d1011"
            else:
                color = "#262b2b"
            label = Label(master=master, text=fields[counter], fg="white", width=18, font="Arial 14",
                          bg=color, pady=0, padx=0)
            label.grid(row=counter, column=0, sticky="ns")
            value_label = Label(master=master, text="", fg="white", width=18, font="Arial 14",
                                bg=color, pady=0, padx=0)
            value_label.grid(row=counter, column=1, sticky="ns")
            Grid.rowconfigure(master, counter, weight=1)

            self.collection[counter] = value_label
        Grid.columnconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 1, weight=0)

    def set_params(self, params_values):
        for i in self.collection:
            self.collection.get(i).configure(text=str(params_values[i]))


class UserInterface(object):
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title(u"Графическая оболочка приложения")
        self.main_window.configure(background="#e7e4e3")
        self.main_window.geometry("1024x720")
        self.main_window.wm_resizable(False, False)

        self.right_frame = Frame(self.main_window, bg="#e7e4e3")
        self.right_frame.grid(row=1, column=2, rowspan=2, sticky=NSEW)

        self.left_frame = Frame(self.main_window, bg="#e7e4e3")
        self.left_frame.grid(row=1, column=0, columnspan=2, sticky=NSEW)

        self.HELLO_USER = Label(self.main_window,
                                background="#262b2b",
                                height=4,
                                text=u"Приложение для определения принадлежности выборки к нормальному "
                                     u"распределению\nс помощью критерия \"Хи-квадрат\" Пирсона", fg="white"
                                ).grid(column=0, row=0, columnspan=3, sticky="we")

        self.panel = Label(self.main_window, bg="#5f787b")
        self.panel.grid(row=1, column=0, columnspan=2, sticky=NSEW)

        self.FIELDS = [u"Степени свободы", u"Среднее", u"Дисперсия", u"Хи квадрат", u"Распределение"]

        self.right_panel = EquationParamsWidget(self.FIELDS, self.right_frame)
        Grid.columnconfigure(self.main_window, 0, weight=1)
        Grid.columnconfigure(self.main_window, 1, weight=0)
        Grid.rowconfigure(self.main_window, 1, weight=1)

        self.path_str = Entry(self.main_window)

        self.path_str.grid(row=2, column=0, sticky="we")
        self.path_str.insert(0, u"Путь к файлу")
        self.path_str['state'] = "disabled"

        ftype = [("Текстовые файлы", "*.txt")]
        dialog = filedialog.Open(filetypes=ftype)
        self.fl = ""

        def choose_file():
            self.fl = dialog.show()
            if self.fl != "":
                self.path_str['state'] = "normal"
                self.path_str.delete(0, END)
                self.path_str.insert(0, self.fl)
                self.path_str['state'] = "readonly"
                h_ = 0.001
                significance_ = 0.05
                self.right_panel.set_params(algorithm.main(h_, significance_, self.fl))
                parts = self.fl.split("/")
                self.image = ImageTk.PhotoImage(file=parts[len(parts) - 1].split(".")[0] + ".jpg")
                self.img = Label(self.main_window, image=self.image)
                self.img.grid(row=1, column=0, columnspan=2)

        self.load_file_btn = Button(master=self.main_window, bg="#e7e4e3", text=u"Загрузить файл", fg="#0d1011",
                                    command=choose_file)
        self.load_file_btn.grid(row=2, column=1, sticky="we")
        self.load_file_btn.bind()
        Grid.rowconfigure(self.main_window, 2, weight=0)
        Grid.rowconfigure(self.main_window, 1, weight=1)
        self.main_window.mainloop()

    def set_params_values(self, values):
        self.right_panel.set_params(values)

    def get_file_path(self):
        return self.fl


if __name__ == '__main__':
    gui = UserInterface()
