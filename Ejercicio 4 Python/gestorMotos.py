from claseMoto import Moto
import csv

class GestorMoto:
    __listaMotos : list
    def __init__(self):
        self.__listaMotos = []
    
    def agregarMoto(self, unaMoto):
        self.__listaMotos.append(unaMoto)

    def testMotos(self):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                "Saltear Cabecera"
                bandera = not bandera
            else:
                patente = fila[0]
                marca = fila[1]
                nombre = fila[2]
                apellido= fila[3]
                km= fila[4]
                unaMoto = Moto(patente,marca,nombre,apellido,km)
                self.agregarMoto(unaMoto)
        archivo.close()
    

    def validarMoto(self, patente):
        indice = 0
        valorDeRetorno = None
        bandera= False
        while not bandera and indice < len(self.__listaMotos):
            if self.__listaMotos[indice].getPatente() == patente:
                bandera = True
                valorDeRetorno = indice
            else:
                indice += 1
        return valorDeRetorno

    def mostrarConductor(self,patent):
        indice = 0
        valorderetorno = None
        bandera = False
        while not bandera and indice< len(self.__listaMotos):
            if self.__listaMotos[indice].getPatente() == patent:
                print(f"{self.__listaMotos[indice]}")
                bandera = True
                valorderetorno = indice
            else:
                indice+=1
        return valorderetorno
    
    def ListadoMotos(self, GP):
        for i in range(len(self.__listaMotos)):
            print("------------------------------------------------------")
            print(f"Patente de moto: {self.__listaMotos[i].getPatente()}")
            print(f"Conductor: {self.__listaMotos[i].getNombre()} {self.__listaMotos[i].getApellido()}")
            GP.ListadoMotoP(self.__listaMotos[i].getPatente())
