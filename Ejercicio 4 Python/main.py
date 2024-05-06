from gestorMotos import GestorMoto
from gestorPedido import GestorPedidos

def opcion0(GM,GP):
    print('Adios')

def opcion1(GM,GP):
    patente= input("Ingrese patente del pedido: ")
    indice = GM.validarMoto(patente)
    if indice == None:
        print("Moto Inalida")
    else:
        print("Moto Valida")
        GP.cargarNuevosPedidos(patente)

def opcion2(GM,GP):
    patent = input("Ingrese patente del pedido: ")
    ide = input("Ingrese Id del pedido: ")
    tiempoR = float(input("Ingrese tiempo real de entrega: "))
    GP.ModificarTiempo(patent,ide,tiempoR)

def opcion3(GM,GP):
    patent = input("Ingrese patente: ")
    indice = GM.mostrarConductor(patent)
    if indice != None:
        GP.Promedio(patent)
    else:
        print("Patente no encontrada")

def opcion4(GM,GP):
    GM.ListadoMotos(GP)
    

def opcion5(GM,GP):
    GP.mostrarPedidos()

def opcion6(GM,GP):
    GP.ordenar()

switcher = {
 0: opcion0,
 1: opcion1,
 2: opcion2,
 3: opcion3,
 4: opcion4,
 5: opcion5,
 6: opcion6
}

def switch(opcion,GM,GP):
    func = switcher.get(opcion, lambda: print("Opción incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3 or opcion  == 4 or opcion == 5 or opcion == 6:
        func(GM,GP)
    else:
         func()
   

if __name__ == '__main__':
    GM = GestorMoto()
    GM.testMotos()
    GP= GestorPedidos()
    GP.testPedidos()
    bandera = False
    while not bandera:
        print("\n---------MENU---------")
        print("1- Agregar pedido")
        print("2- Modificar tiempo de entrega")
        print("3- Mostrar datos del conductor")
        print("4- Listado motos")
        print("5- Mostrar pedidos")
        print("6- Ordenar Pedidos")
        print("0- SALIR")
        opcion = int(input ('\nIngrese una opcion: '))
        switch(opcion, GM,GP)
        bandera = int(opcion) == 0