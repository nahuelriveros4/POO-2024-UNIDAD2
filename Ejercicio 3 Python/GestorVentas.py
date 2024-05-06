class GestordeVentas:
    __ventas : list
    def __init__(self):
        self.__ventas = [[0 for _ in range(7)] for _ in range(5)]

    def registrarVenta (self, dia, sucursal, importe):
        self.__ventas[sucursal][dia] = self.__ventas[sucursal][dia] + importe
    
    def totalSucursal (self,sucursal):
        total = 0
        for j in range (7):
            total = total + self.__ventas[sucursal][j]
        print(f"\nEl total facturado de la sucursal {sucursal + 1} es ${total}")
    
    def obtenerSucursal(self, dia):
        maxFacturacion = -1000
        sucursal = None
        for i in range (5):
            if self.__ventas[i][dia] > maxFacturacion:
                maxFacturacion = self.__ventas[i][dia]
                sucursal = i+1
        print(f"La sucursal {sucursal} facturó ${maxFacturacion}")


    def sucursalMenor(self):
        menorFacturacion = 99999999
        sucursal = None
        for i in range (5):
            totalsucursal=0
            for j in range (7):
                totalsucursal = totalsucursal + self.__ventas[i][j]
                if totalsucursal < menorFacturacion:
                    menorFacturacion = totalsucursal
                    sucursal = i+1
        print(f"La sucursal {sucursal} es la que menos facturó con un total de ${menorFacturacion}")
                
    def TotalFacturado(self):
        total=0
        for i in range(5):
            for j in range (7):
                total = total + self.__ventas[i][j]
        print(f"El total facturado es ${total}")
