#VIDEO 10 TAREA 1

# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.



from multiprocessing.sharedctypes import Value
import sys
import tkinter
from tkinter import IntVar, Label, ttk
from tkinter import messagebox


window =tkinter.Tk()
window.title('Elige tu país')
window.geometry('250x300')

def tueleccion():
    te = seleccion.get()
    if te ==1:
        output="Argentina"
    elif te ==2:
        output="Brasil"
    elif te ==3:
        output="Canadá"
    elif te ==4:
        output="China"
    elif te ==5:
        output="Escocia"
    else:
        output="Seleccion inválida"

    return messagebox.showinfo('Elige tu país',f'Has seleccionado {output}.')


def limpiar():
   seleccion.set(None)

seleccion=IntVar() 

sel1 =ttk.Radiobutton(window, text='Argentina', value ='1',variable =seleccion, command=tueleccion)
sel2 =ttk.Radiobutton(window, text='Brasil', value ='2',variable =seleccion, command=tueleccion)
sel3 =ttk.Radiobutton(window, text='Canadá', value ='3',variable =seleccion, command=tueleccion)
sel4 =ttk.Radiobutton(window, text='China', value ='4',variable =seleccion, command=tueleccion)
sel5 =ttk.Radiobutton(window, text='Escocia', value ='5',variable =seleccion, command=tueleccion)

sel1.grid(column=1,row=0,padx=80,pady=7)
sel2.grid(column=1,row=1,padx=80,pady=7)
sel3.grid(column=1,row=2,padx=80,pady=7)
sel4.grid(column=1,row=3,padx=80,pady=7)
sel5.grid(column=1,row=4,padx=80,pady=7)



reset=ttk.Button(window, text='Limpiar',command=limpiar)
reset.grid(column=1, row=7,sticky=tkinter.W,padx=5,pady=5)

window.mainloop()
sys.exit() 
