from classTransaccion import Transaccion
import csv

class GestorTransaccion:
    __listaTransaccion:list
    def __init__(self):
        self.__listaTransaccion = []
    
    def agregarTransaccion(self, unaTrans):
        self.__listaTransaccion.append(unaTrans)

    def testArchivo(self):
        archivo = open('transaccionesBilletera.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "Saltear cabecera"
                bandera = not bandera
            else:
                Cvu = fila[0]
                NumTransaccion = fila[1]
                Importe =float(fila[2])
                TipoTransaccion =  fila[3]
                unaTrans=Transaccion(Cvu,NumTransaccion,Importe, TipoTransaccion)
                self.agregarTransaccion(unaTrans)
        archivo.close()


    def sumarTrans(self, cvu):
        suma=0
        for i in range(len(self.__listaTransaccion)):
            if self.__listaTransaccion[i].getCVU() == cvu:
                suma = suma + self.__listaTransaccion[i].getImporte()
        return suma
    
    def mostrar(self):
        for i in range(len(self.__listaTransaccion)):
            print(f"\n{self.__listaTransaccion[i]}")

