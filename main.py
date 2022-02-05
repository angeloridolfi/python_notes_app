from tkinter import *
from random import randint


def nota():
    def aoclicar():
        while True:
            cont = 1
            #notes["text"] += f"\nNota {cont}:\n" + entry.get()  # <<<===== TENTAR ARRUMAR!
            cont += 1
            if nota():
                break

    entrada = Tk()
    entrada.title("Adicionar uma nota!")
    entrada.geometry('200x100')
    digit = Label(entrada, text="Digite aqui:")
    digit.pack()
    entry = Entry(entrada)
    entry.pack()
    anota = Button(entrada, text="ADICIONAR", bg="red", fg="white", command=aoclicar)
    anota.pack()
    entrada.mainloop()



main = Tk()
main.geometry("800x600")
main.title("Notas")
titulo = Label(text="Hello World!", font="impact 20 bold")
titulo.pack()

add_note = Button(main, text="Adicionar uma nota", bg="red", fg="white", command=nota)
add_note.pack()

#notes = Label(main, text="", font="arial 20 italic", fg=cores[color_random])
#notes.pack()

color_random = randint(0, 4)
main.mainloop()
