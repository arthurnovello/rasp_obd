import gui
import threading
from sensores import dist, temp
from buzz import buz

class Main():
    def __init__(self):
        self.numPessoas = 0
        self.motorista = dist(4, 17)
        # self.carona = dist(27, 22)
        # self.passageiro = dist(5, 6)
        self.temperatura = 0
        self.umidade = 0
        self.fumaca = False
        self.alerta = False

    def atualizaDados(self):
        self.numPessoas = 0
        self.motorista = dist(4, 17)
        if self.motorista < 30:
            self.numPessoas += 1
        # if self.carona < 30:
        #     self.numPessoas += 1
        # if self.passageiro < 30:
        #     self.numPessoas += 1
        self.temperatura = temp("TEMP")
        self.umidade = temp("HUMID")
        self.fumaca = False     #sensor de fumaca -----> Não Instalado

    def disparaAlarme(self):
        if (self.temperatura > 37 or self.temperatura < 0 or self.fumaca == True or self.umidade < 70) and self.numPessoas >= 1:
            buz("ON")
            self.alerta = True
        else:
            buz("OFF")
            self.alerta = False

main = Main()
tela = gui.Gui()

def atualizaGui():
    while True:
        main.atualizaDados()
        main.disparaAlarme();
        tela.popularInfos(main.temperatura, main.umidade, main.numPessoas, main.fumaca, main.alerta)

thread = threading.Thread(target=atualizaGui)
thread.start()
tela.window.mainloop()
