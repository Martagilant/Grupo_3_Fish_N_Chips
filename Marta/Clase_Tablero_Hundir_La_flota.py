
class Tablero:

    def __init__(self, tamano, jugador_id, barcos,tablero_impacto):
        self.tamano = tamano
        self.tablero = self.CrearVacio(tamano)
        self.jugador_id = jugador_id
        self.barcos = barcos # Diccionario con barcos y sus esloras
        self.tablero_impacto = tablero_impacto #tablero para los impactos
        
    def CrearVacio(self, tamano):
        tablero = np.full((tamano,tamano)," ")
        print(tablero)
        return tablero
    
    
    def ubicador_barcos(self, eslora, ubicacion, orientacion):
        fila, columna = ubicacion
        if orientacion == "n":   #Orientacion N, el barco se colocará hacia arriba. La fila de inicio menos la eslora no sea menor que 0  
            if fila - eslora + 1 < 0:
                print("No se puede poner un barco en esa posición")
                return False
        elif orientacion == "s": #Orientación es S, el barco se colocará hacia abajo. La fila de inicio más la eslora no salga del tablero
            if fila + eslora > self.tamano:
                print("No se puede poner un barco en esa posición")
                return False
        elif orientacion == "e": #E, el barco a la dcha. La columna de inicio más la eslora no salga tablero.
            if columna + eslora > self.tamano:
                print("No se puede poner un barco en esa posición")
                return False
        elif orientacion == "o": #O, el barco se colocará hacia la izq. La columna de inicio menosbjl la eslora no salga tablero.
            if columna - eslora + 1 < 0:
                print("No se puede poner un barco en esa posición")
                return False
        else:
            print("Orientación no válida, solo n, s, e, o")
            return False
        
        for i in range(eslora): #colocar barcos y que no haya ninguno ya ahi
            if self.tablero[fila, columna] == "O":
                print("Ya hay un barco en esa posición")
                return False
            
            self.tablero[fila, columna] = "O"
            
            if orientacion == "n":
                fila -= 1
            elif orientacion == "s":
                fila += 1
            elif orientacion == "e":
                columna += 1
            elif orientacion == "o":
                columna -= 1
        
        print(self.tablero)
        return True    
    
    
    
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
        
        orientacion = random.choice(["n","s","e","o"])
        ubicacion = [random.randint(0,self.tamano),random.randint(0,self.tamano)]
        self.ubicador_barcos(eslora,ubicacion,orientacion)
        return self.tablero
    
    def colocar_BarcoManual(self):
        """ el jugador coloca los barcos manualmente mediante input."""
        for eslora, cantidad in self.barcos.items():
            for _ in range(cantidad):
                colocado = False
                while not colocado:
                    try:
                        print(f"Colocando barco de {eslora} casillas.")
                        fila = int(input("Introduce la fila (0-9): "))
                        columna = int(input("Introduce la columna (0-9): "))
                        orientacion = input("Orientación (n para norte, s para sur, e para este, o para oeste): ").lower()
                        
                        if orientacion not in ["n", "s", "e", "o"]:
                            print("Orientación no válida. Usa n, s, e, o.")
                            continue
                        
                        if self.ubicador_barcos(eslora, [fila, columna], orientacion):
                            colocado = True
                        else:
                            print("Posición inválida. Inténtalo de nuevo.")
                    except ValueError:
                        print("Entrada inválida. Asegúrate de introducir números enteros.")
#Comprueba que no salga