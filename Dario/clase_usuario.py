import numpy as np
class Usuario:
    

    def __init__(self, nombre, vidas = 20, barcos = 10, barcos_hundidos = 0,
                 tablero_barcos = np.full((10,10), " "), tablero_disparos = np.full((10,10), " ")):
        self.nombre = nombre
        self.vidas = vidas
        self.barcos = barcos
        self.barcos_hundidos = barcos_hundidos
        self.tablero_barcos = tablero_barcos
        self.tablero_disparos = tablero_disparos

    def coloca_barco(self):
        pass
    
    def disparo_maquina(self):
        pass

    def disparo_jugador(self):
        pass

    def visualizar_tablero(self):
        pass

jugador = Usuario("Jugador")


maquina = Usuario("Máquina")

print(jugador.nombre)