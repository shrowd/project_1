from tkinter import *
import subprocess
import inicjaly
import obiekty3d


def run_game():
    try:
        process = subprocess.Popen(['python', 'gra.py'], shell=False)
    except OSError as e:
        print("Error: ", e)


def objects3d():
    if var.get() == 1:
        obiekty3d.draw("teapot")
    elif var.get() == 2:
        obiekty3d.draw("spoon")
    elif var.get() == 3:
        obiekty3d.draw("cup")


okno = Tk()
var = IntVar()
okno.title("Projekt 1")
okno.geometry("250x150")

t1 = Label(okno, text="Wybierz zadanie:", width=20)
t1.grid(row=1, column=1)

p1 = Button(okno, text="Inicjały", width=10, command=inicjaly.draw)
p1.grid(row=2, column=1)

p2 = Button(okno, text="gra", width=10, command=run_game)
p2.grid(row=3, column=1)

p3 = Button(okno, text="Obiekt 3d", width=10, command=objects3d)
p3.grid(row=4, column=1)

t2 = Label(okno, text="Wybierz obiekt:")
t2.grid(row=1, column=2)

r1 = Radiobutton(okno, text="teapot", variable=var, value=1)
r1.grid(row=2, column=2)
r1.select()

r2 = Radiobutton(okno, text="spoon", variable=var, value=2)
r2.grid(row=3, column=2)

r3 = Radiobutton(okno, text="cup", variable=var, value=3)
r3.grid(row=4, column=2)

okno.mainloop()
