import numpy as np
import pandas as pd

class Tablero:

    def __init__(self, name, tamano, jugador_id, barcos, impactos):
        self.tamano = tamano
        self.name = name
        self.tablero = self.CrearVacio(tamano)
        self.jugador_id = jugador_id
        self.barcos = barcos # Diccionario con barcos y sus esloras
        self.impactos = impactos #tablero para los impactos
        
    def CrearVacio(self, tamano):
        tablero = np.full((tamano,tamano)," ")
        print(tablero)
        return tablero
    
         
    
    def ubicador_barcos(self, eslora,ubicacion, orientacion):
        

        for i in range(eslora):
          
            if ubicacion[0] <0 or ubicacion[0] > self.tamano or ubicacion[1] <0 or ubicacion[1] > self.tamano:
                print("No se puede poner un barco en esa posición")
                break
            if self.tablero[ubicacion[0],ubicacion[1]] == "O":
                print("Ya hay un barco en esa posición")
                break
        
            self.tablero[ubicacion[0],ubicacion[1]] = "O"
        
            if orientacion == "n":
                ubicacion[0] = ubicacion[0] - 1
            elif orientacion == "s":
                ubicacion[0] = ubicacion[0] + 1
            elif orientacion == "e":
                ubicacion[1] = ubicacion[1] + 1
            elif orientacion == "o":
                ubicacion[1] = ubicacion[1] - 1
            else:
                print("Orientación no válida, solo n,s,e,o")
                break
        print(self.tablero)
        return self.tablero
    
    def disparo(self, ubicacion):
        if ubicacion[0] <0 or ubicacion[0] > self.tamano or ubicacion[1] <0 or ubicacion[1] > self.tamano:
            print("No se puede disparar a esa posición")
            
        elif self.tablero[ubicacion[0],ubicacion[1]] == "O":
            print("Tocado")
            self.tablero[ubicacion[0],ubicacion[1]] = "X"
        elif self.tablero[ubicacion[0],ubicacion[1]] == " ":
            self.tablero[ubicacion[0],ubicacion[1]] = "-"
            print("Agua")
        else:
            print("Ya habías disparado ahí")
        print(self.tablero)
        return self.tablero
    
    def BarcoAleatorio(self, eslora):
        
        orientacion = np.random.choice(["n","s","e","o"])
        ubicacion = [np.random.randint(0,self.tamano),np.random.randint(0,self.tamano)]
        self.ubicador_barcos(eslora,ubicacion,orientacion)
        return self.tablero
    
tablero_1 = Tablero("Tablero_Barcos_1", 10, "jugador", 10, 0)
tablero_2 = Tablero("Tablero_Disparos_1", 10, "jugador", 10, 0)
