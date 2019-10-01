import gui
import threading
from sensores import dist, temp
from buzz import buz
from time import sleep


while True:
    # Confere se tem alguem nas posicoes motorista, carona e passageiro
    print("ok while")
    motorista = dist(4, 17)
    print(motorista)
    # carona = dist(27, 22)
    # passageiro = dist(5, 6)
    if motorista < 30:
        print("ok if")
        # if motorista < 30 or carona < 30 or passageiro < 30:
        if temp("TEMP") <= 27 and temp("TEMP") >= 10:
            buz("OFF")
            # Mostra tela de tudo ok
        elif (temp("TEMP") > 27 or temp("TEMP") < 10) and \
             (temp("TEMP") <= 37 or temp("TEMP") >= 0):
            buz("OFF")
            # Mostra tela de Alerta
        elif temp("TEMP") > 37 or temp("TEMP") < 0:
            buz("ON")
            # Mostra tela de Emergencia
    sleep(1)
tela = gui.Gui()
def atualizaGui(tela,temp,pessoas,fumaca):
    while True:    
        tela.popularInfos(tela.temp,tela.pessoas,tela.fumaca)
        tela.temp = temp
        tela.pessoas = pessoas
        tela.fumaca = fumaca
        sleep(1)

thread = threading.Thread(target=atualizaGui,args=(tela,temp,pessoas,fumaca))
thread.start()
tela.window.mainloop()        
