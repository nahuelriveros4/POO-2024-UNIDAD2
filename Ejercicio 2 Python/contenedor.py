from claseCajaAhorro import CajaAhorro
class Lista:
    __cajas: list
    def __init__(self):
        self.__cajas = []
    
    def agregarCaja(self,unaCaja):
        self.__cajas.append(unaCaja)
    
    def mostrarCajas(self):
        for caja in self.__cajas:
            caja.mostrarDatos()

    def CuentaBancaria (self):
        Cuil = input("Ingrese Cuil: ")
        self.BuscarCuil(Cuil)

    def BuscarCuil (self, cuil):
        indice = 0
        valorDeRetorno = None
        band = False
        while not band and indice < len(self.__cajas):
            if self.__cajas[indice].getCuil() == cuil:
                band= True
                valorDeRetorno = indice
            else:
                indice +=1
        self.ObtenerDatosCta(valorDeRetorno)

    def ObtenerDatosCta(self,indice):
        if indice != None:
            print("\n---DATOS DE LA CUENTA---\n")
            self.__cajas[indice].mostrarDatos()
        else:
            print("\nCUIL NO ENCONTRADO\n")