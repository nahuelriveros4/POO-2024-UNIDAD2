from clasePedido import Pedido
import csv

class GestorPedidos:
    __listaPedidos = list
    def __init__(self):
        self.__listaPedidos=[]

    def agregarPedido(self,unPedido):
        self.__listaPedidos.append(unPedido)

    def testPedidos(self):
        archivo = open('datosPedidos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                "Saltear Cabecera"
                bandera = not bandera
            else:
                patente = fila[0]
                IDpedido = fila[1]
                comidasPedidas = fila[2]
                tiempoEstimado = float(fila[3])
                tiempoReal = float(fila[4])
                precioPedido = float(fila[5])
                unPedido= Pedido(patente,IDpedido,comidasPedidas,tiempoEstimado,tiempoReal,precioPedido)
                self.agregarPedido(unPedido)
        archivo.close()
    

    def cargarNuevosPedidos(self, patente):
        print("\nIngrese datos del nuevo pedido ")
        Idpedido= input("Ingrese ID del pedido: ")
        comidas=input("Ingrese comidas pedidas: ")
        tiempoEstimado= float(input("Ingrese tiempo estimado de entrega: "))
        tiempoReal= float(input("Ingrese tiempo real de entrega: "))
        precio= float(input("Ingrese precio del pedido: $"))
        unPedido= Pedido(patente,Idpedido,comidas, tiempoEstimado, tiempoReal,precio)
        self.agregarPedido(unPedido)

    def ModificarTiempo(self,patente, ide, tiempor):
        indice = 0
        valorderetorno = None
        bandera = False
        while not bandera and indice < len(self.__listaPedidos):
            if self.__listaPedidos[indice].getPatentePedido()==patente and self.__listaPedidos[indice].getIDpedido()== ide and self.__listaPedidos[indice].getTiempoReal()==tiempor:
                bandera = True
                valorderetorno = indice
            else:
                indice +=1
        self.nuevotiempo(valorderetorno)

    def nuevotiempo(self,indice):
        if indice != None:
            nuevotiempo= float(input("Ingrese nuevo tiempo real: "))
            self.__listaPedidos[indice].modificatiempo(nuevotiempo)
        else:
            print("Pedido no encontrado")

    def Promedio(self,patente):
        total = 0
        promedio = 0
        cont=0
        for fila in range(len(self.__listaPedidos)):
            if self.__listaPedidos[fila].getPatentePedido() == patente:
                total += self.__listaPedidos[fila].getTiempoReal()
                cont +=1
        promedio = total / cont
        print(f"El promedio de tiempo real de entrega es de {promedio}")


    def ListadoMotoP (self, patent):
        print("ID Pedido     Tiempo Estimado      Tiempo real    Precio")
        total = 0
        comision = 0
        for i in range(len(self.__listaPedidos)):
            if self.__listaPedidos[i].getPatentePedido() == patent:
                total += self.__listaPedidos[i].getPrecioPedido()
                print(f"{self.__listaPedidos[i].getIDpedido()}             {self.__listaPedidos[i].getTiempoEst()}m               {self.__listaPedidos[i].getTiempoReal()}m           ${self.__listaPedidos[i].getPrecioPedido()}  ")
                comision= (total*20)/100
        print(f"Total:                                              ${total}")    
        print(f"Comision: ${comision}")


    def ordenar (self):
        pedidosOrdenados = sorted(self.__listaPedidos)
        for fila in pedidosOrdenados:
            print(f"{fila}\n")

    def mostrarPedidos(self):
        for fila in self.__listaPedidos:
            print(f"{fila}\n")
