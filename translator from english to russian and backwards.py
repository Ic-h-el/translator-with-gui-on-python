from tkinter import *
from translate import Translator

root = Tk()
root.title("Translator by Ilya Bychkov")

choice1 = StringVar(root)
choice2 = StringVar(root)

choices = {"Английский": "en", "Русский": "ru"}

choice1.set("Английский")
choice2.set("Русский")

def translate():
    translator = Translator(from_lang=choices[choice1.get()], to_lang=choices[choice2.get()])
    translation = translator.translate(var.get())
    var1.set(translation)

choice1Menu = OptionMenu(root, choice1, *choices.keys())
Label(root, text="Выберите язык перевода").grid(row=0, column=1)
choice1Menu.grid(row=1, column=1)

choice2Menu = OptionMenu(root, choice2, *choices.keys())
Label(root, text="Выберите исходный язык").grid(row=0, column=2)
choice2Menu.grid(row=1, column=2)

Label(root, text = "Введите текст").grid(row=2, column=0)
var = StringVar()
textbox = Entry(root, textvariable = var).grid(row=2, column=1)

Label(root, text = "Результат перевода").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(root, textvariable = var1).grid(row=2, column=3)

b = Button(root, text = "Перевести", command=translate, relief=GROOVE).grid(row = 3, column = 1, columnspan = 3)

mainloop()