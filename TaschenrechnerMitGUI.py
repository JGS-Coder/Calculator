from tkinter import StringVar, Tk
import tkinter as tk
from tkinter import messagebox
import math

# ideen: mit dem ergebnis weiterrechnen, brüche

# Create Window, set title and set background color
root = Tk()
root.title("Taschenrechner mit GUI")
root.geometry("350x500")
root.configure(bg="#929fa2")

PARAMS = None

textin = StringVar()
operator = ""

# Title
labelTop = tk.Label(root, bg="#929fa2",
                    text="Calculator", font=("Calibri", 22, 'bold'))
labelTop.place(x=75, y=3)


def PressT(number):
    global operator
    operator = operator+str(number)
    textin.set(operator)


def PressSQRT():
    global operator
    try:
        operator = str(math.sqrt(eval(operator)))
    except SyntaxError:
        messagebox.showerror(title="Fehler", message=" Keine gültige Eingabe")
    except ValueError:
        messagebox.showerror(title="Fehler", message="Wurzel ziehen im Minus-"
                                                     "Bereich nicht möglich")
    except TypeError:
        messagebox.showerror(title="Fehler", message="Ungültige Eingabe!")
    textin.set(operator)


def gleich():
    global operator
    if not operator:
        messagebox.showerror(title="Fehler", message="Keine gültige Eingabe")
        return
    op = ""
    try:
        op = str(eval(operator))
    except ZeroDivisionError:
        messagebox.showerror(title="Fehler", message="Division durch 0 nicht "
                             "möglich")
    except SyntaxError:
        messagebox.showerror(title="Fehler", message="Ungültige Eingabe!")
    except TypeError:
        messagebox.showerror(title="Fehler", message="Ungültige Eingabe!")
    textin.set(op)
    operator = ''


def DelLast():
    global operator
    operator = operator[:-1]
    textin.set(operator)


def clrbut():
    global operator
    textin.set('')
    operator = ''


def quit():
    root.destroy()


# Ausgabefeld

e1 = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin,
              width=25, bd=15)
e1.place(x=35, y=50)
e1.configure(state='disabled')

# Buttons


T1 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14, text='1',
               command=lambda: PressT(1))
T1.place(x=25, y=325, width=65, height=65)

T2 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14,
               pady=14, text='2', command=lambda: PressT(2))
T2.place(x=95, y=325, width=65, height=65)

T3 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14,
               text='3', command=lambda: PressT(3))
T3.place(x=165, y=325, width=65, height=65)

T4 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14,
               text='4', command=lambda: PressT(4))
T4.place(x=25, y=255, width=65, height=65)

T5 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14,
               text='5', command=lambda: PressT(5))
T5.place(x=95, y=255, width=65, height=65)

T6 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14,
               pady=14, text='6', command=lambda: PressT(6))
T6.place(x=165, y=255, width=65, height=65)

T7 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14, text='7',
               command=lambda: PressT(7))
T7.place(x=25, y=185, width=65, height=65)

T8 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14,
               pady=14, text='8', command=lambda: PressT(8))
T8.place(x=95, y=185, width=65, height=65)

T9 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14,
               text='9', command=lambda: PressT(9))
T9.place(x=165, y=185, width=65, height=65)

T0 = tk.Button(root, font=("Calibri", 15, 'bold'), padx=14, pady=14, bd=4,
               command=lambda: PressT(0), text="0")
T0.place(x=25, y=400, width=125, height=75)

TKlaOn = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                   bd=4, command=lambda: PressT("("), text="(")
TKlaOn.place(x=120, y=115, width=50, height=50)

TKlaOff = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                    bd=4, command=lambda: PressT(")"), text=")")
TKlaOff.place(x=175, y=115, width=50, height=50)

TSQRT = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                  bd=4, command=lambda: PressSQRT(), text="√")
TSQRT.place(x=230, y=115, width=50, height=50)

TPu = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                bd=4, command=lambda: PressT("."), text=".")
TPu.place(x=160, y=400, width=80, height=75)

TPlus = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14, bd=4,
                  text="+", command=lambda: PressT("+"))
TPlus.place(x=240, y=170, width=45, height=45)

TMinus = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                   bd=4, text="-", command=lambda: PressT("-"))
TMinus.place(x=290, y=170, width=45, height=45)

TMal = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                 bd=4, text="*", command=lambda: PressT("*"))
TMal.place(x=290, y=220, width=45, height=45)

TPot = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                 bd=4, text="x^x", command=lambda: PressT("**"))
TPot.place(x=285, y=115, width=50, height=50)

TPuPu = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                  bd=4, text="/", command=lambda: PressT("/"))
TPuPu.place(x=240, y=220, width=45, height=45)

TCE = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'),
                pady=119, bd=4, text="CE", command=clrbut)
TCE.place(x=240, y=335, width=95, height=60)

TDEL = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'),
                 pady=119, bd=4, text="DEL", command=DelLast)
TDEL.place(x=240, y=270, width=95, height=60)

TGleich = tk.Button(root, padx=151, font=("Calibri", 15, 'bold'),
                    pady=14, bd=4, command=gleich, text="=")
TGleich.place(x=250, y=400, width=85, height=75)

TExit = tk.Button(root, text="Beenden", font=("Calibri", 15, 'bold'),
                  command=root.destroy)
TExit.place(x=25, y=115, width=90, height=50)

root.mainloop()
