from tkinter import *
from calculate import calculate

def show(val):
    if resultField.get('0.0', END) == '0\n':
        resultField.delete("0.0", END)
        resultField.insert(INSERT, val)
    else:
        ops = {'-', '+', '*', '/', ' '}
        prev = resultField.get("0.0", 'end-1c')
        resultField.delete("0.0", END)
        if (prev[len(prev) - 1] not in ops) and val == '( ':
            prev += ' * '
        prev += val
        resultField.insert(INSERT, prev)

def clear():
    resultField.delete('0.0', END)
    resultField.insert(INSERT, '0')

def calc():
    exp = resultField.get("0.0", 'end-1c')
    res = calculate(exp)
    resultField.delete('0.0', END)
    resultField.insert(INSERT, str(res))

window = Tk()

window.wm_title("Calculator")

resultField = Text(window, height=1, width=15)
resultField.insert(INSERT, "0")
resultField.grid(row=1, column=1, columnspan=3)

b9 = Button(window, text="9", width=5, command=lambda : show("9"))
b9.grid(row=2, column=3)

b8 = Button(window, text="8", width=5, command=lambda : show("8"))
b8.grid(row=2, column=2)

b7 = Button(window, text="7", width=5, command=lambda : show("7"))
b7.grid(row=2, column=1)

b6 = Button(window, text="6", width=5, command=lambda : show("6"))
b6.grid(row=3, column=3)

b5 = Button(window, text="5", width=5, command=lambda : show("5"))
b5.grid(row=3, column=2)

b4 = Button(window, text="4", width=5, command=lambda : show("4"))
b4.grid(row=3, column=1)

b3 = Button(window, text="3", width=5, command=lambda : show("3"))
b3.grid(row=4, column=3)

b2 = Button(window, text="2", width=5, command=lambda : show("2"))
b2.grid(row=4, column=2)

b1 = Button(window, text="1", width=5, command=lambda : show("1"))
b1.grid(row=4, column=1)

bdiv = Button(window, text="/", width=5, command=lambda : show(" / "))
bdiv.grid(row=2, column=4)

dmul = Button(window, text="x", width=5, command=lambda : show(" * "))
dmul.grid(row=3, column=4)

bminus = Button(window, text="-", width=5, command=lambda : show(" - "))
bminus.grid(row=4, column=4)

badd = Button(window, text="+", width=5, command=lambda : show(" + "))
badd.grid(row=5, column=4)

bOpenParen = Button(window, text="(", width=5, command=lambda : show("( "))
bOpenParen.grid(row=5, column=2)

bCloseParen = Button(window, text=")", width=5, command=lambda : show(" ) "))
bCloseParen.grid(row=5, column=3)

b0 = Button(window, text="0", width=5, command=lambda : show("9"))
b0.grid(row=5, column=1)

bClear = Button(window, text="C", width=10, command=lambda : clear())
bClear.grid(row=6, column=1, columnspan=2)

bCalc = Button(window, text="=", width=10, command=lambda : calc())
bCalc.grid(row=6, column=3, columnspan=2)

window.mainloop()