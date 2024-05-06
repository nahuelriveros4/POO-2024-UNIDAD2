from contenedor import Lista
from claseCajaAhorro import CajaAhorro
def test ():
    c1 = CajaAhorro('0012555', '202033069', 'Gonzalez', 'Jorge', 20550.90)
    c2 = CajaAhorro('2554999', '279498899', 'Perez', 'Luis', 200.90)
    c3 = CajaAhorro('4564866', '275991669', 'Vargas', 'Juan', 500000.90)
    c4 = CajaAhorro('2005589', '542469788', 'Diaz', 'Maria', 50090)
    c5 = CajaAhorro('6497564', '301255979', 'Mercado', 'Ana', 20800.50)
    listaCajas = Lista()
    listaCajas.agregarCaja(c1)
    listaCajas.agregarCaja(c2)
    listaCajas.agregarCaja(c3)
    listaCajas.agregarCaja(c4)
    listaCajas.agregarCaja(c5)
    listaCajas.mostrarCajas()
    listaCajas.CuentaBancaria()