from gestorCuenta import GestorCuentas
from gestorTransaccion import GestorTransaccion

def opcion0(GC,GT):
    print("\nAdios")

def opcion1(GC,GT):
    dni = input("\nIngrese DNI del cliente: ")
    cvu=GC.mostrarDatos(dni)
    saldo=GT.sumarTrans(cvu)
    GC.mostrarinforme(saldo,cvu)

def opcion2(GC,GT):
    por= float(input("\nIngrese nuevo porcentaje: "))
    GC.modificarPorcentaje(por)

def opcion3(GC,GT):
    GC.ActualizarSaldo()

def opcion4(GC,GT):
    cvu = input("\nIngrese CVU del cliente: ")
    saldo=GT.sumarTrans(cvu)
    GC.mostrarinforme(saldo,cvu)

def opcion5(GC,GT):
    GC.guardar_datos_en_csv()                                


def opcion6(GC,GT):
    GC.mostrar()
    GT.mostrar()

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6
}

def switch(opcion, GC,GT):
    func = switcher.get(opcion, lambda: print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3 or opcion ==4 or opcion == 5 or opcion == 6:
        func(GC,GT)
    else:
        func()

if __name__=='__main__':
    GC = GestorCuentas(3)
    GT = GestorTransaccion()
    GT.testArchivo()
    GC.testArchivo()

    bandera = False
    while not bandera:
        print("\n------MENU------")
        print("1 - Informar datos del cliente")
        print("2 - Modificar porcentaje anual")
        print("3 - Actualizar saldo")
        print("4 - Informar saldo inicial y saldo actualizado")
        print("5 - Almacenar Datos en un archivo")
        print("6 - Mostrar")
        print("0 - SALIR")
        opcion = int(input("\nIngrese opcion: "))
        switch(opcion,GC,GT)
        bandera = int(opcion) == 0
