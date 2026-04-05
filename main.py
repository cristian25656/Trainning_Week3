from ui.menus import *
from src.funciones import *
from db.csv import *
def validar_numero(mensaje, tipo=float):
    """Valida que la entrada sea numérica y no negativa."""
    continuar_validacion = True
    resultado = 0
    
    while continuar_validacion:
        try:
            entrada = input(mensaje)
            valor = tipo(entrada)
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                resultado = valor
                continuar_validacion = False  # Rompemos el ciclo de validación
        except ValueError:
            print("Error, ingrese un numero.")
    return resultado
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
            nombre_buscado = input("Digite el nombre del producto a buscar: ")
            resultado = buscar_producto(inventario, nombre_buscado)
            if resultado:
                print(f"Producto encontrado: {resultado}")
            else:
                print("Producto no encontrado.")
        elif opcion == 4:
            nombre_producto = input("Nombre del producto a editar: ")
            precio_producto = validar_numero("Nuevo precio (0 para omitir): ")
            cantidad_producto = validar_numero("Nueva cantidad (0 para omitir): ", int)
            if actualizar_producto(inventario, nombre_producto, precio_producto or None, cantidad_producto or None):
                print(" Producto actualizado.")
            else: print("No se encontró el producto.")
        elif opcion == 5:
            nombre_eliminar = input("Digite el nombre del producto a eliminar: ")
            confirmar = input(f"""
¿Está seguro de eliminar '{nombre_eliminar}'? 
digite: (si/no): 
""")
            if confirmar == "si":
                if eliminar_producto(inventario, nombre_eliminar):
                    print(f"El producto {nombre_eliminar} ha sido eliminado.")
                else:
                    print("No se encontró el producto para eliminar.")
            elif confirmar == "no":
                print("Producto eliminado")
            else:
                print("valor invalido")
        elif opcion == 6:
            if not inventario:
                print("El inventario está vacío. No se puede calcular")
            else:
                v_total, c_unidades, total_registros, mas_caro, mayor_stock = calcular_estadisticas(inventario)
                print(f"""
Estadisticas:
Cantidad de productos: {total_registros}
Total de unidades: {c_unidades}
Valor total: {v_total}

Producto más caro: {mas_caro['nombre']} (${mas_caro['precio']})
Producto con más stock: {mayor_stock['nombre']} ({mayor_stock['cantidad']} unidades)
""")
        elif opcion == 7:
            guardar_csv(inventario, "inventario.csv")

        elif opcion == 8:
            datos, filas_error = cargar_csv("inventario.csv")
            if datos is not None:
                print(f"Se encontraron {len(datos)} productos y {filas_error} errores.")
                op = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                
                if op == 'S':
                    inventario = datos
                    print("[OK] Inventario reemplazado.")
                else:
                    for p_nuevo in datos:
                        p_existente = buscar_producto(inventario, p_nuevo['nombre'])
                        if p_existente:
                            p_existente['cantidad'] += p_nuevo['cantidad']
                            p_existente['precio'] = p_nuevo['precio'] # Actualiza al precio más reciente
                        else:
                            inventario.append(p_nuevo)
                    print("[OK] Inventario fusionado (Cantidades sumadas).")

        elif opcion == 9:
            print("Hasta pronto")
            inicio = 0
            
    except ValueError:
        print("Digite un valor valido")
