class Equipo:
    __idEquipo:int
    __NombreEquipo:str
    __golesFavor: int
    __golesContra:int
    __difGoles:int
    __puntos:int
    def __init__(self, ide,nom,golf,golc,dif,puntos) :
        self.__idEquipo = ide
        self.__NombreEquipo = nom
        self.__golesFavor = golf
        self.__golesContra = golc
        self.__difGoles=dif
        self.__puntos = puntos

    
    def __str__(self) -> str:
        return (f"ID: {self.__idEquipo}\n"
                f"Nombre: {self.__NombreEquipo}\n"
                f"Goles a Favor: {self.__golesFavor}\n"
                f"Goles en Contra: {self.__golesContra}\n"
                f"Dif. Goles: {self.__difGoles}\n"
                f"Puntos: {self.__puntos}")
    
    def getID(self):
        return self.__idEquipo
    
    def getNombre(self):
        return self.__NombreEquipo
    
    def getGolesFavor(self):
        return self.__golesFavor
    
    def getGolesContra(self):
        return self.__golesContra
    
    def getDifGoles(self):
        return self.__difGoles
    
    def getPuntos(self):
        return self.__puntos