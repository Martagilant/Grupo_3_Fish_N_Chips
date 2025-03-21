import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QAction, qApp, QMenu


# Creamos la clase de la venta principal
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
        
        
    # Definimos las acciones las opciones de los menús
    def opcion_1(self):
        self.texto.setText('Has elegido la opción 1 del menú principal')

    def opcion_2(self):
        self.texto.setText('Has elegido la opción 2 del menú principal')

    def opcion_a(self):
        self.texto.setText('Has elegido la opción a del submenú')

    def opcion_b(self):
        self.texto.setText('Has elegido la opción b del submenú')


if __name__ == '__main__':

    # creamos una aplicación PyQT
    aplicacion = QApplication([])

    # creamos la ventana principal
    ventana = VentanaPrincipal()
    ventana.show()

    # ejecutamos la aplicación y terminamos el programa al cerrarse la ventana
    sys.exit(aplicacion.exec())