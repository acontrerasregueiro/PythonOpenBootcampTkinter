#Iniciacion con tkinter crear una ventana
#Importamos los componentes necesarios
#EJEMPLO GEOMETRIA PACK 
#cuando queremos posicionar elementos de arriba a abajo o cara a cara (izq-der)

import tkinter

window = tkinter.Tk() #Creamos una instancia de tk


label1 = tkinter.Label(window,text= "Label1", bg='yellow', fg='blue') #creamos un label
label1.pack(ipadx=45,ipady=15 ,fill='x', side='left') 
label2 = tkinter.Label(window,text= "Label2", bg='orange', fg='green') #creamos un label
label2.pack(ipadx=45,ipady=15 ,fill='x', side='left') 
label3 = tkinter.Label(window,text= "Label3", bg='blue', fg='red') #creamos un label
label3.pack(ipadx=45,ipady=15, side='left') 
label4 = tkinter.Label(window,text= "Label4", bg='yellow', fg='black') #creamos un label
label4.pack(ipadx=45,ipady=15 ,fill='x', side='left') 

label_adios = tkinter.Label(window,text= 'adios', bg='red', fg='white')
label_adios.pack(ipadx=50,ipady=50,side='left')



window.mainloop()# Bucle necesario