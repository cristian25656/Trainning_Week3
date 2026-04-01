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
def buscar_producto(id,nombre):
    for i in id:
        ()