import numpy as np
import random

#import Clase_Tablero_Hundir_La_flota as tb
dict_barcos = {
    "Carrier": 2,
    "Battleship":4,
    "Cruiser": 1,
    "Submarine": 2,
    "Destroyer": 3,
}
class Usuario:
    

    def __init__(self, nombre, barcos = dict_barcos, barcos_hundidos = 0):
        self.nombre = nombre
        self.barcos = barcos
        self.barcos_hundidos = barcos_hundidos
        self.tablero_barcos = np.full((10,10)," ") #Falta importar clase tablero y poner un tablero creado ahí
        self.tablero_disparos = np.full((10,10)," ") #Falta importar clase tablero y poner un tablero creado ahí
        self.vidas = self.calcula_vidas()


    def coloca_barco(self):
        pass # llamar a la función de clase barco
    
    def disparo_maquina(self):
        ubicacion = [random.randint(0,len(self.tablero_disparos)-1),random.randint(0,len(self.tablero_disparos)-1)] #Limita el aleatorio a las dimensiones del tablero
        print(ubicacion)
        while self.tablero_disparos[ubicacion[0],ubicacion[1]] == "X" or self.tablero_disparos[ubicacion[0],ubicacion[1]] == "-": #Verifica si no se ha hecho ese disparo anteriormente
            ubicacion = [random.randint(0,len(self.tablero_disparos)-1),random.randint(0,len(self.tablero_disparos)-1)]
        
        if jugador.tablero_barcos[ubicacion[0], ubicacion[1]] == "O":
            jugador.tablero_barcos[ubicacion[0], ubicacion[1]] = "X" #Marca el acierto en el tablero de barcos del jugador
            self.tablero_disparos[ubicacion[0], ubicacion[1]] = "X" #Marca el acierto en el tablero de disparos de la máquina
            return True #Para controlar el bucle while en el que irá incluido y saber si sigue disparando o no
        else:
            jugador.tablero_barcos[ubicacion[0], ubicacion[1]] = "-" #Marca el fallo
            self.tablero_disparos[ubicacion[0], ubicacion[1]] = "-"
            return False
        

    def disparo_jugador(self):
        coordenada_1 = input("Introduce la fila (del 1 al 10): ") #Pide las coordenadas una a una para una conversión más sencilla
        coordenada_1
        while int(coordenada_1) > 10 or int(coordenada_1) < 1: #Verifica que se haya metido una coordenada válida y si no la vuelve a pedir
            print("La coordenada no puede ser mayor de 10")
            coordenada_1 = input("Introduce la fila (del 1 al 10): ")
        coordenada_2 = input("Introduce la columna: ")
        coordenada_2
        while int(coordenada_2) > 10 or int(coordenada_1) < 1:
            print("La coordenada no puede ser mayor de 10")
            coordenada_2 = input("Introduce la columna: ")
        ubicacion = [int(coordenada_1)-1, int(coordenada_2)-1] 

        if maquina.tablero_barcos[ubicacion[0], ubicacion[1]] == "O": #mismo mecanismo que disparo máquina
            maquina.tablero_barcos[ubicacion[0], ubicacion[1]] = "X"
            self.tablero_disparos[ubicacion[0], ubicacion[1]] = "X"
            return True
        if maquina.tablero_barcos[ubicacion[0], ubicacion[1]] == "X" or maquina.tablero_barcos[ubicacion[0], ubicacion[1]] == "-": #avisa al jugador si ya ha disparado ahí pero el turno lo pierde igual
            print("Ya has disparado ahí")
            return False
        else:
            maquina.tablero_barcos[ubicacion[0], ubicacion[1]] = "-"
            self.tablero_disparos[ubicacion[0], ubicacion[1]] = "-"
            return False
    
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

maquina = Usuario("Máquina")

