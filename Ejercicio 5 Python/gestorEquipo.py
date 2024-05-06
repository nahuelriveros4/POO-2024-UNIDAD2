from classEquipo import Equipo
import numpy as np
import csv

class GestorEquipo:
    __cantidad :int
    __dimension: int
    __incremento = 5
    __arregloEquipos = np.ndarray
    def __init__(self, dimension, incremento = 5) :
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__arregloEquipos = np.empty(dimension, dtype=Equipo)

    def agregarEquipo(self,unEquipo):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__arregloEquipos.resize(self.__dimension)
        self.__arregloEquipos[self.__cantidad]=unEquipo
        self.__cantidad +=1

    def testArchivo(self):
        archivo = open('equipos2024.csv', encoding='utf-8-sig')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "Saltear cabecera"
                bandera = not bandera
            else:
                idEquipo = int(fila[0])
                NombreEquipo = fila[1]
                golesFavor = int(fila[2])
                golesContra = int(fila[3])
                difGoles =int(fila[4])
                puntos= int(fila[5])
                unEquipo = Equipo(idEquipo,NombreEquipo,golesFavor,golesContra,difGoles,puntos)
                self.agregarEquipo(unEquipo)
        archivo.close()

    
    def mostrar(self):
        for i in self.__arregloEquipos:
            print("--------------")
            print(f"{self.__arregloEquipos[i]}")