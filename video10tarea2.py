#VIDEO 10 TAREA 2
# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter
from tkinter.font import Font

ventana=tkinter.Tk()
ventana.title('Que color prefieres?')
ventana.geometry('300x200')

colores=tkinter.StringVar(value=['hot pink','aquamarine','peach puff','yellow2','doger blue'])

frame = tkinter.Frame()
frame = tkinter.LabelFrame(ventana, text='Elige tu color', padx=80, bg= '#dddddd')
frame.pack()

color = tkinter.Label(frame, text='Los colores hablan de tí',bg='light grey', fg='blue')
color.pack(ipadx=50, ipady=8, fill='both')

listbox=tkinter.Listbox(frame,height=10,activestyle=tkinter.NONE,highlightcolor="dark green",highlightbackground="SpringGreen4",bg='darkOliveGreen1', fg="#000",selectforeground="#ffffff",selectbackground="#00aa00",selectborderwidth=3
 ,font=Font(family="Courier", size=10),borderwidth=2 ,listvariable=colores)
listbox.pack(ipadx=150, ipady=50, fill='both')


ventana.mainloop()
