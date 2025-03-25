import numpy as np
import pandas as pd
import clase_usuario as cu
import constantes as cs
import clase_barco_2 as cb
import random
import Clase_Tablero_Hundir_La_flota_2 as tablero
import time

np.random.seed(42)

jugador = cu.jugador
maquina = cu.maquina
jugador.coloca_barcos_aleatorio()
maquina.coloca_barcos_aleatorio()
jugador.vidas = jugador.calcula_vidas()
maquina.vidas = maquina.calcula_vidas()

while jugador.vidas > 0 and maquina.vidas > 0:
    print("Es tu turno")
    print("Tus disparos:", jugador.tablero_disparos, "Tus barcos:", jugador.tablero_barcos, sep="\n")
    while jugador.disparo_jugador() == True:
        print("Es tu turno")
        print("Tus disparos:", jugador.tablero_disparos, "Tus barcos:", jugador.tablero_barcos, sep="\n")
        time.sleep(15)

    print("Es el turno de la máquina")
    print("Los disparos de la máquina:", maquina.tablero_disparos, "Los barcos de la máquina:", maquina.tablero_barcos, sep="\n")    
    while maquina.disparo_maquina() == True:
        print("Es el turno de la máquina")
        print("Los disparos de la máquina:", maquina.tablero_disparos, "Los barcos de la máquina:", maquina.tablero_barcos, sep="\n")
        time.sleep(15)

    

        
        

