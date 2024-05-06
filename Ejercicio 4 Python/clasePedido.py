class Pedido:
    __patente : str
    __IDpedido : str
    __comidasPedidas : str
    __tiempoEstimado :float
    __tiempoReal=0
    __precioPedido: float
    def __init__(self, patente, idpedido, comidas, tiempoestimado, tiempoReal, precio):
        self.__patente = patente
        self.__IDpedido = idpedido
        self.__comidasPedidas = comidas
        self.__tiempoEstimado = tiempoestimado
        self.__tiempoReal = tiempoReal
        self.__precioPedido = precio

    def __str__(self):
        return (f"Pedido {self.__IDpedido} asignado a moto {self.__patente}, "
                f"contiene {(self.__comidasPedidas)}, tiempo estimado {self.__tiempoEstimado} min, "
                f"precio total ${self.__precioPedido}. Tiempo real de entrega: {self.__tiempoReal} min.")
    
    def getPatentePedido(self):
        return self.__patente
    
    def getIDpedido(self):
        return self.__IDpedido
    
    def getComidas(self):
        return self.__comidasPedidas
    
    def getTiempoEst(self):
        return self.__tiempoEstimado
    
    def getTiempoReal(self):
        return self.__tiempoReal
    
    def getPrecioPedido(self):
        return self.__precioPedido
    
    def modificatiempo(self, nuevot):
        self.__tiempoReal=nuevot
    
    def __lt__(self, other): 
        # Sobrecarga del operador < para comparar por patente de moto
        return self.__patente < other.__patente