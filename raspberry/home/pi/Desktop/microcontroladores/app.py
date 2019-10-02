import gui
import threading
# from sensores import dist, temp
# from buzz import buz
from time import sleep


# while True:
    # numPessoas = 0
    # motorista = dist(4, 17)
    # carona = dist(27, 22)
    # passageiro = dist(5, 6)

    # if motorista < 30:
    #     numPessoas += 1
    # if carona < 30:
    #     numPessoas += 1
    # if passageiro < 30:
    #     numPessoas += 1

    # temperatura = temp("TEMP")
    # umidade = temp("HUMID")
    # pessoas = numPessoas 
    # fumaca = False     #sensor de fumaca -----> Não Instalado
    
#PARA TESTES
temperatura = 30
umidade = 12
pessoas = 3
fumaca = False     #sensor de fumaca -----> Não Instalado
alerta = True

    # #verificar essas condicoes para disparar o alarme(ACRESCENTAR UMIDADE E PESSOAS)
    # if temperatura <= 27 and temperatura >= 10:
    #     buz("OFF")
    #     alerta = False
    # elif (temperatura > 27 or temperatura < 10) and (temperatura <= 37 or temperatura >= 0):
    #     buz("OFF")
    #     alerta = False
    # elif temperatura > 37 or temperatura < 0:
    #     buz("ON")
    #     alerta = True
    
tela = gui.Gui()
def atualizaGui(tela,temperatura,umidade,pessoas,fumaca,alerta):
    while True:    
        tela.popularInfos(tela.temperatura, tela.umidade, tela.pessoas,tela.fumaca,tela.alerta)
        tela.temperatura = temperatura
        tela.umidade = umidade
        tela.pessoas = pessoas
        tela.fumaca = fumaca
        tela.alerta = alerta
        sleep(1)

thread = threading.Thread(target=atualizaGui,args=(tela,temperatura,umidade,pessoas,fumaca,alerta))
thread.start()
tela.window.mainloop()        
