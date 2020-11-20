import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Calculator")


rezultat = tk.Entry(window, width=35, borderwidth=3, font=("Arial", 22))
rezultat.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=10, sticky="nsew")


# Functii

def btn_click(numar):
    c = rezultat.get()
    rezultat.delete(0, END)
    rezultat.insert(0, str(c) + str(numar))

def btn_clear():
    rezultat.delete(0, END)

def btn_adunare():
    numar_unu = rezultat.get()
    global numar
    global math
    math = "adunare"
    numar = int(numar_unu)
    rezultat.delete(0, END)

def btn_egal():
    numar_doi = rezultat.get()
    rezultat.delete(0, END)

    if math == "adunare":
        rezultat.insert(0, numar + int(numar_doi))
    if math == "minus":
        rezultat.insert(0, numar - int(numar_doi))
    if math == "inmultire":
        rezultat.insert(0, numar * int(numar_doi))
    if math == "impartire":
        rezultat.insert(0, numar / int(numar_doi))

def btn_minus():
    numar_unu = rezultat.get()
    global numar
    global math
    math = "minus"
    numar = int(numar_unu)
    rezultat.delete(0, END)

def btn_inmultire():
    numar_unu = rezultat.get()
    global numar
    global math
    math = "inmultire"
    numar = int(numar_unu)
    rezultat.delete(0, END)

def btn_impartire():
    numar_unu = rezultat.get()
    global numar
    global math
    math = "impartire"
    numar = int(numar_unu)
    rezultat.delete(0, END)


# Definire Butoane

btn_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: btn_click(0))
btn_adunare = tk.Button(window, text="+", padx=40, pady=20, command=btn_adunare)
btn_egal = tk.Button(window, text="=", padx=40, pady=20, command=btn_egal)
btn_clear = tk.Button(window, text="C", padx=40, pady=20, command=btn_clear)
btn_minus = tk.Button(window, text="-", padx=40, pady=20, command=btn_minus)
btn_inmultire = tk.Button(window, text="*", padx=40, pady=20, command=btn_inmultire)
btn_impartire = tk.Button(window, text="/", padx=40, pady=20, command=btn_impartire)


# Asezare butoane pe ecran

btn_clear.grid(row=1, column=0, columnspan=3, sticky="nsew")
btn_impartire.grid(row=1, column=3, columnspan=1, sticky="nsew")

btn_7.grid(row=2, column=0, columnspan=1, sticky="nsew")
btn_8.grid(row=2, column=1, columnspan=1, sticky="nsew")
btn_9.grid(row=2, column=2, columnspan=1, sticky="nsew")

btn_inmultire.grid(row=2, column=3, columnspan=1, sticky="nsew")

btn_4.grid(row=3, column=0, columnspan=1, sticky="nsew")
btn_5.grid(row=3, column=1, columnspan=1, sticky="nsew")
btn_6.grid(row=3, column=2, columnspan=1, sticky="nsew")

btn_minus.grid(row=3, column=3, columnspan=1, sticky="nsew")

btn_1.grid(row=4, column=0, columnspan=1, sticky="nsew")
btn_2.grid(row=4, column=1, columnspan=1, sticky="nsew")
btn_3.grid(row=4, column=2, columnspan=1, sticky="nsew")
btn_adunare.grid(row=4, column=3, columnspan=1, sticky="nsew")

btn_0.grid(row=5, column=0, columnspan=2, sticky="nsew")
btn_egal.grid(row=5, column=2, columnspan=2, sticky="nsew")

window.mainloop()
