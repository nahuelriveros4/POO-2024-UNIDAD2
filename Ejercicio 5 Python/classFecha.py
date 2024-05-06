class Fecha:
    __FechaPartido:str
    __IdLocal:int
    __IdVisita: int
    __GolLocal:int
    __GolVisita:int
    def __init__(self, fecha, idl,idv,goll,golv) :
        self.__FechaPartido = fecha
        self.__IdLocal = idl
        self.__IdVisita = idv
        self.__GolLocal = goll
        self.__GolVisita=golv

    
    def __str__(self) -> str:
        return (f"Fecha Partido: {self.__FechaPartido}\n"
                f"ID Local: {self.__IdLocal}\n"
                f"ID Visita: {self.__IdVisita}\n"
                f"Goles Local: {self.__GolLocal}\n"
                f"Goles Visita: {self.__GolVisita}")
    
    def getFecha(self):
        return self.__FechaPartido
    
    def getIDlocal(self):
        return self.__IdLocal
    
    def getIDvisita(self):
        return self.__IdVisita
    
    def getGolesLocal(self):
        return self.__GolLocal
    
    def getGolesVisita(self):
        return self.__GolVisita
    