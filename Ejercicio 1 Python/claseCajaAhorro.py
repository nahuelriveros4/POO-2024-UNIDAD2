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



    def validar_cuil(self,cuil):
        cuil = cuil.replace("-", "")  # Eliminamos los guiones para trabajar solo con números
        if len(cuil) != 11 or not cuil.isdigit():
            return False  # Verificamos que tenga 11 dígitos y que todos sean numéricos

        # Dígitos multiplicadores según la normativa de ANSES
        multiplicadores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

        # Extraemos el dígito verificador del CUIL
        digito_verificador_esperado = int(cuil[-1])
    
        # Calculamos el dígito verificador
        suma = sum(int(cuil[i]) * multiplicadores[i] for i in range(10))
        resto = suma % 11
        digito_verificador_calculado = 11 - resto

        if digito_verificador_calculado == 11:
            digito_verificador_calculado = 0
        elif digito_verificador_calculado == 10:
            return False  # El dígito verificador no debería ser 10 para un CUIL válido

        # Comparamos el dígito verificador calculado con el último dígito del CUIL
        return digito_verificador_calculado == digito_verificador_esperado


    def ValdarCuil (self):
       cuil = input("Ingrese cuil para validar: ")
       if self.validar_cuil(cuil) == False:
           print("\nCuil Invalido")
       else:
           print("\nCuil valido")