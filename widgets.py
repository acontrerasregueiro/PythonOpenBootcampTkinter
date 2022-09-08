#Ejemplos de diferentes componentes
#Frame, listbox, radio button
import tkinter
from tkinter import ttk 

window = tkinter.Tk() #Creamos una instancia de tk


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3) # El weight es cuantos elementos puedo posicionar

#Ejemplo Listbox
lista = ['Fedira','Linux','Win2', 'MS DOS', 'MAC OS']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window,height = 20,listvariable= lista_items)
listbox.grid(column=0,row=0,sticky=tkinter.W)

#un frame crea un marco donde posicionar elementos
#Ejemplo Frame
frame = ttk.Frame(window)
label = ttk.Label(frame, text ='hola')
label.grid(column=0,row=0,sticky=tkinter.W, padx = 50, pady=50)
frame.grid(column=0,row=0,sticky=tkinter.W)

#Ejemplo de hacer algo al hacer click, con command= mifuncion
def mifuncion():
    print("clickado el radio button")
#Ejemplo radiobutton
selected = tkinter.StringVar() # Todos los radio butons con variable selected perteneceran al mismo grupo
r1 = ttk.Radiobutton(window,text="si", value='1',variable=selected, command=mifuncion)
r2 = ttk.Radiobutton(window,text="no", value='2',variable=selected, command=mifuncion)
r3 = ttk.Radiobutton(window,text="quizas", value='3',variable=selected, command=mifuncion)

r1.grid(column=0,row=1,padx=5,pady=5)
r2.grid(column=0,row=2,padx=5,pady=5)
r3.grid(column=0,row=3,padx=5,pady=5)

window.mainloop()