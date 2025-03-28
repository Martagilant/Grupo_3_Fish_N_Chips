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
#tablero_barcos_jugador = tablero.Tablero(cs.lado_tablero, cu.jugador, cs.dict_barcos, [])
#tablero_disparos_jugador = tablero.Tablero(cs.lado_tablero, cu.jugador, cs.dict_barcos, [])
#tablero_barcos_maquina = tablero.Tablero(cs.lado_tablero, cu.maquina, cs.dict_barcos, [])
#tablero_disparos_maquina = tablero.Tablero(cs.lado_tablero, cu.maquina, cs.dict_barcos, [])

def bucle():
    while jugador.calcula_vidas() > 0 and maquina.calcula_vidas() > 0: #Si jugador y máquina tienen vidas y el jugador no decide terminar la partida se sigue jugando
        time.sleep(5) #Para que sea más juagable y no aparezca todo de golpe
        print("-"*60, "-"*60, sep = "\n") # Líneas para separar los turnos
        print(f"Es tu turno, tienes {jugador.calcula_vidas()} vidas")
        print("Tus barcos:", jugador.tablero_barcos, sep="\n")
        time.sleep(3)
        print("Tus disparos:", jugador.tablero_disparos, sep="\n")
        while jugador.disparo_jugador() == True: #Si el jugador acierta entra en el bucle y vuelve a tirar
            print("Juegas otra vez")
            print("Tus disparos:", jugador.tablero_disparos, sep="\n")
            time.sleep(5)
        if jugador.terminar == True:
            break    # Termina el juego automáticamente si se elige "terminar"
        
        print("-"*60, "-"*60, sep = "\n")
        time.sleep(3)
        print(f"Es el turno de la máquina, le quedan {maquina.calcula_vidas()} vidas")
        time.sleep(2)  
        while maquina.disparo_maquina() == True:
            print("Es el turno de la máquina")
            time.sleep(2)
            print("Los disparos de la máquina:", maquina.tablero_disparos, sep = "\n")
            time.sleep(5)
    print("Se acabó el juego")
    if maquina.calcula_vidas() > jugador.calcula_vidas():
        print("Has perdido, mejor dedícate a otra cosa")
    elif jugador.calcula_vidas() > maquina.calcula_vidas():
        print("Has ganado, ya podrás")


    
bucle()
        
        

