class Transaccion:
    __Cvu: str
    __NumTransaccion: str
    __Importe: float
    __TipoTransaccion: str
    def __init__(self, cvu, numtr, imp, tipo):
        self.__Cvu = cvu
        self.__NumTransaccion = numtr
        self.__Importe = imp
        self.__TipoTransaccion = tipo

    def __str__(self):
        return f"Cvu: {self.__Cvu} Numero de Transaccion: {self.__NumTransaccion} Importe: ${self.__Importe}  Tipo transaccion: {self.__TipoTransaccion}"

    def getCVU (self):
        return self.__Cvu
    
    def getNumTrans (self):
        return self.__NumTransaccion
    
    def getImporte (self):
        return self.__Importe
    
    def getTipo (self):
        return self.__TipoTransaccion
    