import numpy as np
import random


#creamos la clase barco  
class Barco:
    def __init__(self, eslora): #constructor de barco, con una longitud dada para colocarlo en el tablero #necesito TABLERO

        self.eslora = eslora #longitud o posiciones del barco
        self.posiciones = []  #lista con las coordenadas del barco
        

#comprueba si un barco peude ser colocado
    def colocar_barco(self, tablero):
            dimensiones = 10  #tamaño del tablero que creo que puedoquitar
            orientaciones = ["N","S","E","O"]  #direcciones 

            while True: #bucle con while para buscar una posicion valida hasta encontrar una, no se detiene hasta que el barco esta colocado en una posicion correcta
                # asignar fila columna y orientacion aleatoria
                np.random.seed(42)
                fila = random.randint(0,9) #fila aleatoria entre 0 y 9
                columna = random.randint(0,9) #columna aleatoria entre 0 y 9
                orientacion = random.choice(orientaciones) #elige N,S,E,O

                # tengo que crear verificar_espacio para comprobar que el espacio es correcto, entonces IF es correcto, llamamos a posicionar_barco
                if self.verificar_espacio(fila, columna, orientacion, tablero):
                    self.posicionar(fila, columna, orientacion, tablero)  #Colocar el barco
                    break  # salir cuando consiga colorcarlo


    def verificar_espacio(self, fila, columna, orientacion, tablero):
            #verificar si las coordenadas del barco no se salen del tablero y si no hay otros barcos
            for i in range(self.eslora):
                nueva_fila, nueva_columna = self.calcular_coordenadas(fila, columna, orientacion, i)

                #commomprobar si la nueva posicion esta dentro del tablero
                if nueva_fila < 0 or nueva_fila >= 10 or nueva_columna < 0 or nueva_columna >= 10:
                    return False  #si el barco se sale del tablero

                #verificar si ya hay un barco en esa posicin
                if tablero[nueva_fila][nueva_columna] == "O":
                    return False  #si hay un barco en la posicion no se puede colocar

            return True  #Si todo va bien, devuelve True

    def calcular_coordenadas(self, fila, columna, orientacion, paso=1):
        
            #calcula la nueva posicion, tengo dudas
            if orientacion == "N":
                return fila - paso, columna  #subir
            elif orientacion == "S":
                return fila + paso, columna  #bajar
            elif orientacion == "E":
                return fila, columna + paso  #derechoa
            elif orientacion == "O":
                return fila, columna - paso  #izquierda
            

    def posicionar(self, fila, columna, orientacion, tablero):
            #colcoa el barco en las coordenadas que se calculan
            for i in range(self.eslora):
                nueva_fila, nueva_columna = self.calcular_coordenadas(fila, columna, orientacion, i)
                tablero[nueva_fila][nueva_columna] = "O" #marca la posición del barco con O
                self.posiciones.append((nueva_fila, nueva_columna))  #guardar la posicion


Carrier_1 = Barco(2)
Carrier_2 = Barco(2)
Submarine = Barco(2)
Battleship = Barco(4)
Cruiser_1 = Barco(1)
Cruiser_2 = Barco(1)
Cruiser_3 = Barco(1)
Cruiser_4 = Barco(1)
Destroyer_1 = Barco(3)
Destroyer_2 = Barco(3)

dict_barcos = {
    "Carrier_1": Carrier_1,
    "Carrier_2": Carrier_2,
    "Submarine": Submarine,
    "Battleship": Battleship,
    "Cruiser_1": Cruiser_1,
    "Cruiser_2": Cruiser_2,
    "Cruiser_3": Cruiser_3,
    "Cruiser_4": Cruiser_4,
    "Destroyer_1": Destroyer_1,
    "Destroyer_2": Destroyer_2,
}
