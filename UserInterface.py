from tkinter import *
from tkinter import filedialog
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
            label = Label(master=master, text=fields[counter], fg="white", width=15, font="Arial 14",
                          bg=color, pady=0, padx=0)
            label.grid(row=counter, column=0, sticky="ns")
            value_label = Label(master=master, text="", fg="white", width=6, font="Arial 14",
                          bg=color, pady=0, padx=0)
            value_label.grid(row=counter, column=1, sticky="ns")
            Grid.rowconfigure(master, counter, weight=1)

            self.collection[counter] = value_label
        Grid.columnconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 1, weight=0)

    def set_params(self, params_values):
        for i in self.collection:
            self.collection.get(i).configure(text=str(params_values[i]))


def run():
    main_window = Tk()
    main_window.title(u"Графическая оболочка приложения")
    main_window.configure(background="#e7e4e3")
    main_window.geometry("1024x720")
    main_window.wm_resizable(False, False)

    right_frame = Frame(main_window, bg="#e7e4e3")
    right_frame.grid(row=1, column=2, rowspan=2, sticky=NSEW)

    left_frame = Frame(main_window, bg="#e7e4e3")
    left_frame.grid(row=1, column=0, columnspan=2, sticky=NSEW)

    HELLO_USER = Label(main_window,
                       background="#262b2b",
                       height=4,
                       text=u"Приложение для определения принадлежности выборки к нормальному распределению\nс "
                            u"помощью критерия \"Хи-квадрат\" Пирсона",
                       fg="white"
                       ).grid(column=0, row=0, columnspan=3, sticky="we")

    panel = Label(main_window, bg="#5f787b")
    panel.grid(row=1, column=0, columnspan=2, sticky=NSEW)

    FIELDS = [u"Среднее", u"Дисперсия"]

    right_panel = EquationParamsWidget(FIELDS, right_frame)
    Grid.columnconfigure(main_window, 0, weight=1)
    Grid.columnconfigure(main_window, 1, weight=0)
    Grid.rowconfigure(main_window, 1, weight=1)

    path_str = Entry(main_window)

    path_str.grid(row=2, column=0, sticky="we")
    path_str.insert(0, u"Путь к файлу")
    path_str['state'] = "disabled"

    ftype = [("Текстовые файлы", "*.txt")]
    dialog = filedialog.Open(filetypes=ftype)

    def choose_file():
        fl = dialog.show()
        if fl != "":
            path_str['state'] = "normal"
            path_str.delete(0, END)
            path_str.insert(0, fl)
            path_str['state'] = "readonly"
            right_panel.set_params([34.0, 7])

    load_file_btn = Button(master=main_window, bg="#e7e4e3", text=u"Загрузить файл", fg="#0d1011", command=choose_file)
    load_file_btn.grid(row=2, column=1, sticky="we")
    load_file_btn.bind()

    Grid.rowconfigure(main_window, 2, weight=0)
    main_window.mainloop()


if __name__ == '__main__':
    run()
