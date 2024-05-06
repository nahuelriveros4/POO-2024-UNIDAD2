from claseCajaAhorro import CajaAhorro
def test ():
    unaCaja=CajaAhorro('124546', '131999', 'Riveros', 'Nahuel' ,14698.50)
    unaCaja.mostrarDatos()

    importe = float(input("Ingrese importe a extraer: "))
    unaCaja.extraer(importe)

    importe2 = float(input("Ingrese importe a depositar: "))
    unaCaja.depositar(importe2)
    
    
    unaCaja.ValdarCuil()

