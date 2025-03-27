import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QAction, qApp, QMenu
from PyQt5.QtCore import QThread, pyqtSignal
import time

# Aquí estaría tu función bucle()
def bucle():
    import numpy as np
    import pandas as pd
    import clase_usuario as cu
    import constantes as cs
    import clase_barco_2 as cb
    import random
    #import Clase_Tablero_Hundir_La_flota_2 as tablero
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


# Clase que ejecutará el bucle en un hilo separado
class JuegoThread(QThread):
    finished = pyqtSignal()  # Señal para indicar cuando el hilo ha terminado

    def run(self):
        bucle()  # Aquí se ejecuta tu bucle

        # Emitimos la señal cuando termina el hilo
        self.finished.emit()

# Creamos la clase de la ventana principal
class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        # Configuramos la ventana con un título y un tamaño
        self.setWindowTitle('HUNDIR LA FLOTA')
        self.setFixedWidth(800)
        self.setFixedHeight(700)

        # Creamos una etiqueta de texto y la ubicamos en la ventana
        self.texto = QLabel('Este es el juego de hundir la flota')
        self.setCentralWidget(self.texto)

        # Creamos la barra de menús y añadimos un menú
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu('&Opciones de juego')

        # Creamos tres opciones para el menú principal
        opcion_1 = QAction('1.Jugar', menu)
        opcion_1.triggered.connect(self.opcion_1)
        menu.addAction(opcion_1)

        opcion_2 = QAction('2.Acerca de', menu)
        opcion_2.triggered.connect(self.opcion_2)
        menu.addAction(opcion_2)

        # Creamos un submenú que añadimos al menú principal
        submenu = QMenu('&Submenú', menu)
        menu.addMenu(submenu)

        # Añadimos opciones al submenú
        opcion_a = QAction('Opción &a', menu)
        opcion_a.triggered.connect(self.opcion_a)
        submenu.addAction(opcion_a)

        opcion_b = QAction('Opción &b', menu)
        opcion_b.triggered.connect(self.opcion_b)
        submenu.addAction(opcion_b)

        # Creamos un separador y la opción de salir en el menú principal
        menu.addSeparator()

        accion_salir = QAction('&Salir', menu)
        accion_salir.triggered.connect(qApp.quit)
        menu.addAction(accion_salir)

    # Definimos las acciones de las opciones de los menús
    def opcion_1(self):
        self.texto.setText('Has elegido la opción 1 del menú principal')

        # Iniciamos el hilo para ejecutar el bucle
        self.juego_thread = JuegoThread()
        self.juego_thread.finished.connect(self.juego_terminado)
        self.juego_thread.start()

    def opcion_2(self):
        self.texto.setText('Has elegido la opción 2 del menú principal')

    def opcion_a(self):
        self.texto.setText('Has elegido la opción a del submenú')

    def opcion_b(self):
        self.texto.setText('Has elegido la opción b del submenú')

    def juego_terminado(self):
        self.texto.setText('El juego ha terminado.')

if __name__ == '__main__':

    # Creamos una aplicación PyQT
    aplicacion = QApplication([])

    # Creamos la ventana principal
    ventana = VentanaPrincipal()
    ventana.show()

    # Ejecutamos la aplicación y terminamos el programa al cerrarse la ventana
    sys.exit(aplicacion.exec())