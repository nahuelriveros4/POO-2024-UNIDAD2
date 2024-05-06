from GestorVentas import GestordeVentas
gestor=GestordeVentas()
def Menu ():
    opcion=int(input("\nIngrese opcion: "))
    match opcion:
        case 1:
            dia = int(input("Día de la semana (1=Lunes, ..., 7=Domingo): ")) -1
            sucursal = int(input("Número de sucursal (1 a 5): ")) - 1
            importe = float(input("Importe de la factura: "))
            gestor.registrarVenta(dia, sucursal, importe)
            Menu()
        case 2:
            sucursal= int(input("\nIngrese numero de sucursal: ")) - 1
            gestor.totalSucursal(sucursal)
            Menu()
        case 3:
            dia = int(input("\nIngrese dia: "))-1
            gestor.obtenerSucursal(dia)
            Menu()
        case 4:
            gestor.sucursalMenor()
            Menu()
        case 5:
            gestor.TotalFacturado()
            Menu()
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            Menu()
