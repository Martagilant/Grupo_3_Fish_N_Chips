import numpy as np
import random
import constantes as cs
import clase_barco_2 as cb

#import Clase_Tablero_Hundir_La_flota_2 as tablero
np.random.seed(42)
class Usuario:
    

    def __init__(self, nombre, barcos = cb.dict_barcos, barcos_hundidos = 0):
        self.nombre = nombre
        self.barcos = barcos
        self.barcos_hundidos = barcos_hundidos
        self.tablero_barcos = Tablero(10, nombre, barcos, [])
        self.tablero_disparos = Tablero(10, nombre, barcos, [])
        self.vidas = self.calcula_vidas()
        self.terminar = False


    def coloca_barcos_aleatorio(self):
        np.random.seed(42)
        for indice, barco in self.barcos.items():
            barco.colocar_barco(self.tablero_barcos)
        return self.tablero_barcos
    
    def disparo_maquina(self):
        ubicacion = [random.randint(0,len(self.tablero_disparos)-1),random.randint(0,len(self.tablero_disparos)-1)] #Limita el aleatorio a las dimensiones del tablero
        print(ubicacion)
        while self.tablero_disparos[ubicacion[0],ubicacion[1]] == "X" or self.tablero_disparos[ubicacion[0],ubicacion[1]] == "-": #Verifica si no se ha hecho ese disparo anteriormente
            ubicacion = [random.randint(0,len(self.tablero_disparos)-1),random.randint(0,len(self.tablero_disparos)-1)]
        
        if jugador.tablero_barcos[ubicacion[0], ubicacion[1]] == "O":
            jugador.tablero_barcos[ubicacion[0], ubicacion[1]] = "X" #Marca el acierto en el tablero de barcos del jugador
            self.tablero_disparos[ubicacion[0], ubicacion[1]] = "X"
            print("¡Tocado!\nLa máquina te ha dado")
            resultado = True #Marca el acierto en el tablero de disparos de la máquina
            return resultado #Para controlar el bucle while en el que irá incluido y saber si sigue disparando o no
        else:
            jugador.tablero_barcos[ubicacion[0], ubicacion[1]] = "-" #Marca el fallo
            self.tablero_disparos[ubicacion[0], ubicacion[1]] = "-"
            print("¡Agua! La máquina es casi tan mala como tú")
            resultado = False
            return resultado
        

    def disparo_jugador(self):
        coordenada_1 = input("Introduce la fila (del 1 al 10): ") #Pide las coordenadas una a una para una conversión más sencilla
        if coordenada_1 == "terminar":
            jugador.terminar = True
            print("Has elegido terminar el juego")
        else:
            coordenada_1 = int(coordenada_1)
        if type(coordenada_1) == int:
            while coordenada_1 > 10 or coordenada_1 < 1: #Verifica que se haya metido una coordenada válida y si no la vuelve a pedir
                print("La coordenada no puede ser mayor de 10")
                coordenada_1 = input("Introduce la fila (del 1 al 10): ")
            coordenada_2 = input("Introduce la columna (del 1 al 10): ")
            while int(coordenada_2) > 10 or int(coordenada_1) < 1:
                print("La coordenada no puede ser mayor de 10")
                coordenada_2 = input("Introduce la columna: ")
            ubicacion = [int(coordenada_1)-1, int(coordenada_2)-1] 

            if maquina.tablero_barcos[ubicacion[0], ubicacion[1]] == "O": #mismo mecanismo que disparo máquina
                maquina.tablero_barcos[ubicacion[0], ubicacion[1]] = "X"
                self.tablero_disparos[ubicacion[0], ubicacion[1]] = "X"
                print(f"¡Tocado! Vaya máquina\nTu último disparo ha sido {ubicacion[0]+1}, {ubicacion[1]+1}")
                resultado = True
                return resultado
            if maquina.tablero_barcos[ubicacion[0], ubicacion[1]] == "X" or maquina.tablero_barcos[ubicacion[0], ubicacion[1]] == "-": #avisa al jugador si ya ha disparado ahí pero el turno lo pierde igual
                print("Ya has disparado ahí")
                resultado = False
                return resultado
            else:
                maquina.tablero_barcos[ubicacion[0], ubicacion[1]] = "-"
                self.tablero_disparos[ubicacion[0], ubicacion[1]] = "-"
                print("¡Agua! Vaya paquetón")
                resultado = False
                return resultado
    
    def calcula_vidas(self): #Recorre todo el array contado las O, ese es el número de vidas
        contador_vidas = 0
        for vector in self.tablero_barcos:
            for valor in vector:
                if valor == "O":
                    contador_vidas += 1
        return contador_vidas


    def visualizar_tablero(self):
        pass

jugador = Usuario("Jugador")
maquina = Usuario("Maquina")
