#Iniciacion con tkinter crear una ventana
#Importamos los componentes necesarios
#EJEMPLO DE GEOMETRIA GRID
import tkinter
from tkinter import ttk 

window = tkinter.Tk() #Creamos una instancia de tk


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3) # El weight es cuantos elementos puedo posicionar

#Etiqueta usuario
user_label = ttk.Label(window,text='Username :')
user_label.grid(column=0,row=0, sticky=tkinter.W, padx =5, pady = 5)# stikcy para que no se mueva, se quede anclada
#Campo Usuario
user_entry = ttk.Entry(window)
user_entry.grid(column=1,row= 0,sticky=tkinter.E)

#Etiqueta password
pass_label = ttk.Label(window,text='Password :')
pass_label.grid(column=0,row=1, sticky=tkinter.W, padx =5, pady = 5)# stikcy para que no se mueva, se quede anclada
#Campo password
pass_entry = ttk.Entry(window, show= '*')
pass_entry.grid(column=1,row= 1,sticky=tkinter.E)

#Boton
login_button = ttk.Button(window,text='Login')
login_button.grid(column=1,row=3, sticky=tkinter.E, padx= 5, pady= 5)

window.mainloop()# Bucle necesario