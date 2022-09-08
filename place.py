# GEOMETRIA PLACE
#Es la menos utilizada
#La geometria place permite posicionar los elementos de forma absoluta o de forma 
#relativa a una ventana.
#Es decir le pasamos las coordenadas exactas de los componentenes
import random
import tkinter
from tkinter import ttk

window = tkinter.Tk()

colors= ['red','blue','yellow','orange','black','purple']

for x in range(0,10):
    color = random.randint(0,len(colors)-1)
    color2 = random.randint(0,len(colors)-1)
    #POSICIONAMIENTO RANDOM
    #label1 = tkinter.Label(window,text="ETIQUETA", bg=colors[color], fg=colors[color2])
    #label1.place(x = random.randint(0,100), y = random.randint(0,100))

label3 = tkinter.Label(window,text="posicionamiento absoluto", bg='blue', fg='yellow')
label3.place(x = 50, y = 50)
#posicionamiento relativo
label2 = tkinter.Label(window,text="RELATIVO", bg='red', fg='yellow')
label2.place(relx = 1, rely=0.15,relwidth= 0.5, anchor='ne')

window.mainloop()