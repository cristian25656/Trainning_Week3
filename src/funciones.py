def creacion_producto(id,nombre,precio, cantidad):
    producto = {
        "id" : id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    return producto

def mostrar_inventario(productos):
    if not productos:
        print(f"inventario vacio")
    for i in productos:
        print(i)
def buscar_producto(inventario,nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio o cantidad de un producto existente."""
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None: p['precio'] = nuevo_precio
        if nueva_cantidad is not None: p['cantidad'] = nueva_cantidad
        return True
    return False
def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False
def calcular_estadisticas(inventario):
    valor_total = 0
    cantidad_total_unidades = 0
    
    for i in inventario:
        valor_total += i['precio'] * i['cantidad']
        cantidad_total_unidades += i['cantidad']
        
    return valor_total, cantidad_total_unidades, len(inventario)
