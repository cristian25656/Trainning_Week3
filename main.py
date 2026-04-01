from ui.menus import *
from src.funciones import *
inventario = []
inicio = 1
bienvenida_inventario()

while inicio != 0:
    menuprincipal()
    try:
        opcion = int(input("Digite el numero de la opcion: "))
        if opcion == 1:
            id = int(input("Digite el id del producto: "))
            nombre = input("Digite el nombre del producto: ")
            precio = float(input("Digite el precio del producto: "))
            cantidad = int(input("Digita la cantidad: "))
            producto = creacion_producto(id,nombre,precio,cantidad)
            inventario.append(producto)
        elif opcion == 2:
            mostrar_inventario(inventario)
        elif opcion == 3:
            buscar = input("Digite el id del producto: ")
            
        elif opcion == 9:
            print("Hasta pronto")
            inicio = 0
            
    except ValueError:
        print("Digite un valor valido")