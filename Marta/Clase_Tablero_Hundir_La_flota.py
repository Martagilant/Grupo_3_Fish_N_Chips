
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
