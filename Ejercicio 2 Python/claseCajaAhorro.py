class CajaAhorro:
    __nroCuenta=str
    __cuil=str
    __apellido=str
    __nombre=str
    __saldo=float

    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo =saldo

    def mostrarDatos(self):
        print (f"Cuenta: {self.__nroCuenta}\nCuil: {self.__cuil}\nApellido: {self.__apellido}\nNombre: {self.__nombre}\nSaldo: ${self.__saldo}\n")
    
    def extraer (self,importe):
        if self.__saldo >=  importe:
            self.__saldo= self.__saldo - importe
            print(f"Saldo actual: ${self.__saldo}\n")
        else:
            Saldo = self.__saldo - importe
            print(f"Saldo: ${Saldo}")
            print("Saldo Insuficiente\n")

    def depositar (self,importe):
        if importe > 0:
            self.__saldo = self.__saldo + importe
            print(f"Saldo Actual: ${self.__saldo}\n")
        else:
            print("ERROR Saldo Negativo\n")

    def ValidarCUIL(self, cuil):
        if self.__cuil == cuil:
            print("El Cuil es valido\n")
        else: 
            print("El Cuil es incorrecto\n")

    def getCuil(self):
        return self.__cuil
    
    