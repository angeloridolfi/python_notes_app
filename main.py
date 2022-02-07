from tkinter import *
# from random import randint

main = Tk()
main.title("Notas")
main.geometry("800x600")
main.configure(background='dark blue')


def click():
    clique = Tk()
    nomenota = Label(clique, text="Nome da sua nota", font="Impact 13 italic", fg='blue', bg='lightblue')
    nomenota.pack()
    nome_nota = Entry(clique)
    nome_nota.pack()

    def aoclicar():
        n = Label(main, text=nome_nota.get() + '\n' + esc.get(), fg='black', bg='light gray', font='Arial_Black 15 italic')
        n.place(x=400, y=70)

    clique.configure(background='light blue')
    clique.geometry('300x300')
    digit = Label(clique, text="Descrição da sua nota:", font="Impact 13 italic", fg='blue', bg='lightblue')
    digit.pack()
    esc = Entry(clique)
    esc.pack()
    Button(clique, text="Adicionar", command=aoclicar).pack()
    clique.mainloop()


Label(main, text="Notas:", font="Times_New_Roman 20 bold underline", fg='light blue', bg='darkblue').place(x=420, y=0)
Label(main, text="NoteAPP", font='Times_New_Roman 20 bold underline', fg='white', bg='dark blue').place(x=0, y=0)
Button(main, text="Adicionar uma nota", fg='white', bg='red', command=click).place(x=0, y=50)


# notas = Label(main, text='', font='Impact 20')
# notas.pack()

main.mainloop()
