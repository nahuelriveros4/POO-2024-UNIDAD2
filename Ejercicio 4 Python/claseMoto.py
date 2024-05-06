class Moto:
    __Patente : str
    __Marca : str
    __Nombre : str
    __Apellido : str
    __Kilometros : float
    def __init__(self, patente, marca, nombre, apellido, kilometros):
        self.__Patente = patente
        self.__Marca = marca
        self.__Nombre = nombre
        self.__Apellido = apellido
        self.__Kilometros = kilometros
    
    def __str__(self):
        return f"Moto {self.__Marca} con patente {self.__Patente} conducida por {self.__Nombre} {self.__Apellido} con {self.__Kilometros} km de recorrido"

    def getPatente(self):
        return self.__Patente
    
    def getMarca(self):
        return self.__Marca
    
    def getNombre(self):
        return self.__Nombre
    
    def getApellido(self):
        return self.__Apellido
    
    def getKilometros(self):
        return self.__Kilometros