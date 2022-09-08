#Ejemplo eventos tkinter

import tkinter
from tkinter import Button, ttk 

window = tkinter.Tk() #Creamos una instancia de tk

def saludar(event):
    print('Han hecho click en saludar')
    
def saludarDobleClick(event):
    print('Han hecho Doble click en saludar')
    
def salir(event):
    print('ADIOSSSS')
    window.quit()

boton = tkinter.Button(window, text='Haz Click!')
boton.pack()

boton.bind('<Button-1>', saludar) # Button 1 boton primario del raton
boton.bind('<Double-1>', saludarDobleClick) # Button 1 boton primario del raton

botonSalir = tkinter.Button(window, text='Salir!')
botonSalir.pack()
botonSalir.bind('<Button-1>', salir) # Button 1 boton primario del raton


window.mainloop()# Bucle necesario