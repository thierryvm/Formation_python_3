#! /usr/bin/env python3
# coding: utf-8
import tkinter

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variable tkinter")

# Widgets...

var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)

var_label.set("Hello wolrd !")
print("Label: ", var_label.get())

label.pack()

# Boucle principal

app.mainloop()
