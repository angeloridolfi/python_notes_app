from tkinter import *
from tkinter import scrolledtext
# from random import randint

main = Tk()
main.title("Notas")
main.geometry("800x600")
main.configure(background='light salmon')


def click():
    clique = Tk()
    clique.title("ADICIONAR NOTA!")
    nomenota = Label(clique, text="Nome da sua nota", font="Impact 13 italic", fg='blue', bg='lightblue')
    nomenota.pack()
    nome_nota = Entry(clique)
    nome_nota.pack()

    def aoclicar():
        n = scrolledtext.ScrolledText(main, width=30, height=5)
        n.configure(font="Gothic 15 bold", background='lightcyan')
        n.insert(INSERT, nome_nota.get() + '\n' + esc.get())
        n.pack()

    clique.configure(background='light blue')
    clique.geometry('300x300')
    digit = Label(clique, text="Descrição da sua nota:", font="Impact 13 italic", fg='blue', bg='lightblue')
    digit.pack()
    esc = Entry(clique)
    esc.pack()
    Button(clique, text="Adicionar", command=aoclicar).pack()
    clique.mainloop()


Label(main, text="Notas:", font="Times_New_Roman 20 bold underline", fg='white', bg='lightsalmon').pack()
Label(main, text="NoteAPP", font='Times_New_Roman 20 bold underline', fg='white', bg='lightsalmon').place(x=0, y=0)
Button(main, text="Adicionar uma nota", fg='white', bg='red', command=click).place(x=0, y=50)


# notas = Label(main, text='', font='Impact 20')
# notas.pack()

main.mainloop()
