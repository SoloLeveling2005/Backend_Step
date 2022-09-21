import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os

root = Tk()
# frm = ttk.Frame(root, padding=10, width=300, height=300)
# frm.grid()
text_variable = tk.DoubleVar()
spin_box = tk.Spinbox(
    root,
    from_=1.0,
    to=50.0,
    increment=1.0,
    textvariable=text_variable
)

label_choice_expansion = ttk.Label(root, text="Введите расширение файла, доступные(.xlsx,.pptx,.docx)")
input_get_expansion = Entry(root, textvariable=StringVar())


def create():
    spin_box_item = spin_box.get()
    input_get_expansion_item = input_get_expansion.get()
    expansion = [".xlsx",".pptx",".docx"]
    def create_files():
        if input_get_expansion_item in expansion:
            for i in range(1, int(spin_box_item) + 1):
                new_file = open(f"temp/file{i}{input_get_expansion_item}", "w+")
                new_file.write("Привет, тут ты можешь писать что хочешь")
                new_file.close()
                label_choice_expansion.config(text='Файлы успешно созданы)')
                time.sleep(2)
        else:
            label_choice_expansion.config(text='Расширени файла введен некоректно')
    if os.path.isdir('temp'):
        create_files()
    else:
        os.mkdir("temp")
        create_files()

button = ttk.Button(root, text="Создать", command=create)

label_choice_expansion.grid(column=0, row=0, padx=20, pady=20)
input_get_expansion.grid(column=0, row=1, padx=20, pady=20)
spin_box.grid(column=0, row=2, padx=20, pady=20)
button.grid(column=0, row=3, padx=20, pady=20)

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()