import os
import tkinter as tk
from tkinter import ttk

diretorioAtual = os.path.dirname(os.path.abspath(__file__))

class Gui:
    def __init__(self):
        self.temperatura = 0
        self.pessoas = 0
        self.fumaca = False
        self.alerta = False
        self.umidade = 0
        self.window = tk.Tk()
        self.window.title("Dog Mode")
        self.window.resizable(0,0)
        self.infos = tk.Frame(self.window)
        self.infos.grid(column=1, row=0)
        imgDog = tk.PhotoImage(file=diretorioAtual + "//img//dog.gif")
        self.dog = tk.Label(self.window)
        self.dog.image = imgDog
        self.dog.configure(image=imgDog)
        self.dog.grid(column=0, row=0, padx=(30,0), pady=(30))
        self.lblTemp = ttk.Label(self.infos, font=('Arial', 16))
        self.lblTemp.grid(column=1, row=0, padx=(30))
        self.lblUmid = ttk.Label(self.infos, font=('Arial', 16))
        self.lblUmid.grid(column=1, row=1, padx=(30))
        self.lblPeople = ttk.Label(self.infos, font=('Arial', 16))
        self.lblPeople.grid(column=1, row=2, padx=(30))
        self.lblSmoke = ttk.Label(self.infos, font=('Arial', 16))
        self.lblSmoke.grid(column=1, row=3, padx=(30))
        self.lblAlert = ttk.Label(self.infos, font=('Arial', 16))
        self.lblAlert.grid(column=1, row=4, padx=(30))
    
    def popularInfos(self, temp, umidade, people, smoke, alert):
        self.lblTemp["text"] = "Temperatura no carro: " + str(temp) + "º"
        self.lblUmid["text"] = "Umidade no carro: " + str(umidade)
        self.lblPeople["text"] = "Pessoas no carro: " + str(people)
        if smoke == True:
            self.lblSmoke.configure(text="Fumaça detectada!")
        else:
            self.lblSmoke.configure(text="Fumaça não detectada")
        if alert == True:
            self.lblSmoke.configure(text="ALERTA!", foreground="red")

            
