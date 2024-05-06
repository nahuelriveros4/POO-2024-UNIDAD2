from classCuenta import Cuenta
import csv
import numpy as np
class GestorCuentas:
    __cantidad : int
    __dimension: int
    __incremento = 5
    __arregloCuentas: np.ndarray
    def __init__(self, dimension, incremento=5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__arregloCuentas = np.empty(dimension,dtype=Cuenta)
    
    def agregarCuenta(self, unaCuenta):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloCuentas.resize(self.__dimension)
        self.__arregloCuentas[self.__cantidad]=unaCuenta
        self.__cantidad += 1

    def testArchivo (self):
        archivo = open('cuentasBilletera.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "Saltear Cabecera"
                bandera = not bandera
            else:
                Apellido = fila[0]
                Nombre = fila[1]
                Dni = fila[2]
                Telefono = fila[3]
                Saldo = float(fila[4])
                Cvu = fila[5]
                unaCuenta=Cuenta(Apellido,Nombre, Dni,Telefono,Saldo,Cvu)
                self.agregarCuenta(unaCuenta)
        archivo.close()


    def mostrarDatos(self, dni):
        indice = 0
        bandera = False
        while not bandera and indice < len(self.__arregloCuentas):
            if self.__arregloCuentas[indice].getDNI() == dni:
                bandera=True
                return self.__arregloCuentas[indice].getCVU()
            else:
                indice+=1
        print("DNI incorrecto - Cliente no encontrado")

    def mostrarinforme(self, saldo, cvu):
        indice = 0
        bandera = False
        while not bandera and indice < len(self.__arregloCuentas):
            if self.__arregloCuentas[indice].getCVU() == cvu:
                bandera = True
                saldoActual = self.__arregloCuentas[indice].getSaldo() - saldo
                self.__arregloCuentas[indice].modSaldo(saldoActual)
                print(f"DNI: {self.__arregloCuentas[indice].getDNI()}")
                print(f"Apellido: {self.__arregloCuentas[indice].getApellido()}")
                print(f"Nombre: {self.__arregloCuentas[indice].getNombre()}")
                print(f"CVU: {self.__arregloCuentas[indice].getCVU()}")
                print(f"Saldo Inicial: {self.__arregloCuentas[indice].getSaldo()}")
                print(f"Saldo Actualizado: {self.__arregloCuentas[indice].getSaldo()}")
            else:
                indice+=1

    def modificarPorcentaje(self, por):
        porcen=0
        porcen = por/365
        i=0
        while i < (self.__cantidad):
            self.__arregloCuentas[i].modPorcentaje(porcen)
            i+=1


    def ActualizarSaldo(self):
        indice = 0
        while indice < self.__cantidad:
            nuevoSaldo = self.__arregloCuentas[indice].getSaldo()
            nuevoSaldo = nuevoSaldo + nuevoSaldo * self.__arregloCuentas[indice].getPorcentaje() / 100
            print("\n----------------------------------------------------")
            print(f"DNI: {self.__arregloCuentas[indice].getDNI()}")
            print(f"Apellido: {self.__arregloCuentas[indice].getApellido()}")
            print(f"Nombre: {self.__arregloCuentas[indice].getNombre()}")
            print(f"CVU: {self.__arregloCuentas[indice].getCVU()}")
            print(f"Rendimiento diario: {self.__arregloCuentas[indice].getPorcentaje():.2f}%")
            print(f"Saldo Anterior: {self.__arregloCuentas[indice].getSaldo()}")
            print(f"Saldo Actualizado: {nuevoSaldo:.2f}")
            indice = indice + 1


    def guardar_datos_en_csv(self):
    # Abre el archivo CSV en modo escritura
        with open('CuentasActualizadas.csv', 'w', newline='') as archivo_csv:

        # Crea un escritor CSV
            escritor_csv = csv.writer(archivo_csv)

        # Escribe los encabezados
            encabezados = ['Apellido','Nombre','DNI','Telefono','Saldo','CVU']
            escritor_csv.writerow(encabezados)
            
        # Escribe los datos de las cuentas
            for indice in range(self.__cantidad):
                escritor_csv.writerow([self.__arregloCuentas[indice].getApellido(), self.__arregloCuentas[indice].getNombre(), self.__arregloCuentas[indice].getDNI(), self.__arregloCuentas[indice].getTelefono(), self.__arregloCuentas[indice].getSaldo(),self.__arregloCuentas[indice].getCVU()])

    def mostrar (self):
        print("-------------------------------------------------------------------------")
        for i in range(len(self.__arregloCuentas)):
            if self.__arregloCuentas[i] != 0:
                print(f"\n{self.__arregloCuentas[i]}")