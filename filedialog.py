#Ejemplo filedialog tkinter

import tkinter
from tkinter import filedialog

window= tkinter.Tk()
filename = filedialog.askopenfilename()

window.mainloop()