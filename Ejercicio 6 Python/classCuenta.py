class Cuenta:
    __Apellido:str
    __Nombre:str
    __Dni:str
    __Telefono :str
    __Saldo : float
    __Cvu: str
    __PorcentajeRend= 0.18
    def __init__(self, apellido, nombre, dni, tel, saldo,cvu):
        self.__Apellido=apellido
        self.__Nombre=nombre
        self.__Dni=dni
        self.__Telefono = tel
        self.__Saldo = saldo
        self.__Cvu=cvu
    
    def __str__(self) :
        porcentaje_formateado = f"{self.__PorcentajeRend:.2f}"
        return (f"Apellido y Nombre: {self.__Apellido} {self.__Nombre}  "
            f"DNI: {self.__Dni}  "
            f"Tel: {self.__Telefono}  "
            f"Saldo: ${self.__Saldo}   "
            f"Cvu: {self.__Cvu}  "
            f"Rendimiento: {porcentaje_formateado}")
    
    def getApellido(self):
        return self.__Apellido
    
    def getNombre(self):
        return self.__Nombre
    
    def getDNI(self):
        return self.__Dni
    
    def getTelefono (self):
        return self.__Telefono
    
    def getSaldo(self):
        return self.__Saldo
    
    def getCVU(self):
        return self.__Cvu
    
    @classmethod
    def getPorcentaje (cls):
        return cls.__PorcentajeRend
    
    @classmethod
    def modPorcentaje(cls,porcentajeDiario):
        cls.__PorcentajeRend = porcentajeDiario

    def modSaldo(self, nuevoSaldo):
        self.__Saldo = nuevoSaldo