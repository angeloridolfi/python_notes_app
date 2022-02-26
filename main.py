from tkinter import *
from tkinter import scrolledtext
from random import randint

main = Tk()
main.title("Notas")
main.geometry("500x700")
main.configure(background='light salmon')

def aoclicar():
        while True:
            color_random = randint(0,3)
            #color_choice = 0
            color_list = ['lightblue' , 'white', 'pink', 'lightgreen']
            break
        n = scrolledtext.ScrolledText(main, width=30, height=5)
        n.configure(font="Gothic 15 bold", background=color_list[color_random])
        #color_choice += 1
        #if color_choice > 3:
        #    color_choice = 0
        n.pack()
        des = Button(main,text="Apagar Notas", command=n.destroy, fg='white', bg='red')
        des.place(x=200, y=650)


Label(main, text="NoteAPP", font='Times_New_Roman 20 bold underline', fg='white', bg='lightsalmon').pack()
Label(main, text="Notas:", font="Times_New_Roman 20 bold underline", fg='white', bg='lightsalmon').pack()
Button(main, text="Adicionar uma nota", fg='white', bg='red', command=aoclicar).pack()

main.mainloop()
