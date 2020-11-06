from tkinter import StringVar, Tk, Label
import tkinter as tk
from tkinter import messagebox, Menu
import math
from time import strftime

# Create Window, set title and set background color
# If you just copied the Code, make sure you comment out line 13 or download the .ico from the calculator file on github
root = Tk()
root.title("Calculator with GUI")
root.geometry("350x500")
root.configure(bg="#929fa2")
root.iconbitmap("logo_calculator.ico")

PARAMS = None

textin = StringVar()
operator = ""

# Title
labelTop = tk.Label(root, bg="#929fa2",
                    text="Calculator", font=("Calibri", 22, 'bold'))
labelTop.place(x=110, y=3)


# Clock
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 12, 'bold'),
            background='#929fa2',
            foreground='black')


lbl.place(x=3, y=3)
time()


# Functions
def PressT(number):
    global operator
    operator = operator+str(number)
    textin.set(operator)


def PressSQRT():
    global operator
    try:
        operator = str(math.sqrt(eval(operator)))
    except SyntaxError:
        messagebox.showwarning(title="Warning!", message=" Invalid Input!")
    except ValueError:
        messagebox.showwarning(title="Warning!", message="Not possible to take"
                                                     "root in the minus area")
    except TypeError:
        messagebox.showwarning(title="Warning!", message="Invalid Input!")
    textin.set(operator)


def equal():
    global operator
    if not operator:
        messagebox.showwarning(title="Warning!", message=" Invalid Input!")
        return
    op = ""
    try:
        op = str(eval(operator))
    except ZeroDivisionError:
        messagebox.showerror(title="Error", message="Division by zero not "
                             "possible")
    except SyntaxError:
        messagebox.showwarning(title="Error", message=" Invalid Input!")
    except TypeError:
        messagebox.showwarning(title="Error", message=" Invalid Input!")
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


def action_get_info_dialog():
    m_text = "\
************************\n\
Creator: Yannik M.\n\
Release: 21th October 2020\n\
Version: 1.0.3\n\
************************"
    messagebox.showinfo(message=m_text, title="About")


# Creating a short menu
menubar = Menu(root)
help_menu = Menu(root, tearoff=0)
help_menu.add_command(label="Information", command=action_get_info_dialog)
menubar.add_cascade(label="About", menu=help_menu)
root.config(menu=menubar)


# Creating the display

e1 = tk.Entry(root, font=("Courier New", 12, 'bold'), textvar=textin,
              width=25, bd=15)
e1.place(x=35, y=50)
e1.configure(state='disabled')

# Down here, i created the Buttons and call the functions

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

TBraOn = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                   bd=4, command=lambda: PressT("("), text="(")
TBraOn.place(x=120, y=115, width=50, height=50)

TBraOff = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                    bd=4, command=lambda: PressT(")"), text=")")
TBraOff.place(x=175, y=115, width=50, height=50)

TSQRT = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                  bd=4, command=lambda: PressSQRT(), text="√")
TSQRT.place(x=230, y=115, width=50, height=50)

TPo = tk.Button(root, padx=47, font=("Calibri", 15, 'bold'), pady=14,
                bd=4, command=lambda: PressT("."), text=".")
TPo.place(x=160, y=400, width=80, height=75)

TPlus = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14, bd=4,
                  text="+", command=lambda: PressT("+"))
TPlus.place(x=240, y=170, width=45, height=45)

TMinus = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                   bd=4, text="-", command=lambda: PressT("-"))
TMinus.place(x=290, y=170, width=45, height=45)

TMul = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                 bd=4, text="*", command=lambda: PressT("*"))
TMul.place(x=290, y=220, width=45, height=45)

TPow = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                 bd=4, text="x^x", command=lambda: PressT("**"))
TPow.place(x=285, y=115, width=50, height=50)

TDiv = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'), pady=14,
                  bd=4, text="/", command=lambda: PressT("/"))
TDiv.place(x=240, y=220, width=45, height=45)

TCE = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'),
                pady=119, bd=4, text="CE", command=clrbut)
TCE.place(x=240, y=335, width=95, height=60)

TDEL = tk.Button(root, padx=14, font=("Calibri", 15, 'bold'),
                 pady=119, bd=4, text="DEL", command=DelLast)
TDEL.place(x=240, y=270, width=95, height=60)

TEqual = tk.Button(root, padx=151, font=("Calibri", 15, 'bold'),
                    pady=14, bd=4, command=equal, text="=")
TEqual.place(x=250, y=400, width=85, height=75)

TExit = tk.Button(root, text="Quit", font=("Calibri", 15, 'bold'),
                  command=root.destroy)
TExit.place(x=25, y=115, width=90, height=50)

root.mainloop()
