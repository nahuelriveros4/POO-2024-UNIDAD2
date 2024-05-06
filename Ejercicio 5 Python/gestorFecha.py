from classFecha import Fecha
import csv

class GestorFecha:
    __listaFechas:list
    def __init__(self):
        self.__listaFechas = []

    def agregarFecha(self, unaFecha):
        self.__listaFechas.append(unaFecha)
    
    def testArchivo(self):
        archivo = open('')