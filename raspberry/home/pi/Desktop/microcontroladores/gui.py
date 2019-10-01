import os
import tkinter as tk
from tkinter import ttk

diretorioAtual = os.path.dirname(os.path.abspath(__file__))

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dog Mode")
        self.window.resizable(0,0)
        self.infos = tk.Frame(self.window)
        self.infos.grid(column=1, row=0)
        imgDog = tk.PhotoImage(file=diretorioAtual + "\\img\\dog.png")
        self.dog = tk.Label(self.window)
        self.dog.image = imgDog
        self.dog.configure(image=imgDog)
        self.dog.grid(column=0, row=0, padx=(30,0), pady=(30))
        self.lblTemp = ttk.Label(self.infos, font=('Arial', 16))
        self.lblTemp.grid(column=1, row=0, padx=(30))
        self.lblPeople = ttk.Label(self.infos, font=('Arial', 16))
        self.lblPeople.grid(column=1, row=1, padx=(30))
        self.lblSmoke = ttk.Label(self.infos, font=('Arial', 16))
        self.lblSmoke.grid(column=1, row=2, padx=(30))
    
    def popularInfos(self, temp, people, smoke):
        self.lblTemp["text"] = "Temperatura no carro: " + str(temp) + "º"
        self.lblPeople["text"] = "Pessoas no carro: " + str(people)
        if smoke == True:
            self.lblSmoke.configure(text="Fumaça detectada!", foreground="red")
        else:
            self.lblSmoke.configure(text="Fumaça não detectada", foreground="blue")

gui = Gui()
gui.popularInfos(23,3,False)
gui.window.mainloop()