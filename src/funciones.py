# Esta función crea un producto en forma de diccionario
def creacion_producto(id, nombre, precio, cantidad):
    # Aquí usamos llaves {} para crear un diccionario
    # Un diccionario guarda datos en forma de clave:valor
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    # return sirve para devolver el resultado de la función # En este caso, devuelve el diccionario creado para poder usarlo fuera
    return producto

# Esta función muestra todos los productos del inventario
def mostrar_inventario(productos):
    # 'not' invierte el valor; como una lista vacía es False, esto significa "si la lista está vacía"
    if not productos:
        print("Inventario vacío")
        return  # se usa para salir de la función y no seguir ejecutando
    
    # 'for' recorre cada elemento de la lista y i representa cada producto (diccionario)
    for i in productos:
        print(i)  # imprime cada producto

# Esta función busca un producto por su nombre
def buscar_producto(inventario, nombre):
    # Se recorre toda la lista
    for producto in inventario:
        # Se accede al valor usando la clave ["nombre"]
        if producto["nombre"] == nombre:
            return producto  # devuelve el producto encontrado
    
    # Si no encuentra nada, retorna None (nada)
    return None

# Esta función actualiza el precio o la cantidad de un producto
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None): # Parámetros de la función: inventario y nombre son obligatorios;
# nuevo_precio y nueva_cantidad tienen valor por defecto (None), lo que permite no enviarlos y así actualizar solo uno de los dos
    # Llamamos otra función para buscar el producto
    p = buscar_producto(inventario, nombre)
    
    # Si p existe (no es None)
    if p:
        # 'is not None' se usa para saber si el usuario sí envió un valor
        if nuevo_precio is not None:
            p['precio'] = nuevo_precio  # cambia el precio
        
        if nueva_cantidad is not None:
            p['cantidad'] = nueva_cantidad  # cambia la cantidad
        
        return True  # indica que sí se actualizó
    
    return False  # indica que no se encontró el producto

# Esta función elimina un producto del inventario
def eliminar_producto(inventario, nombre):
    # Busca el producto
    producto = buscar_producto(inventario, nombre)
    
    if producto:
        # remove elimina ese elemento de la lista
        inventario.remove(producto)
        return True  # eliminación exitosa
    
    return False  # no se encontró

# Esta función calcula estadísticas del inventario
def calcular_estadisticas(inventario):
    # Variables acumuladoras (empiezan en 0)
    valor_total = 0
    cantidad_total = 0
    
    # Recorremos el inventario
    for i in inventario:
        # Se multiplica precio * cantidad para obtener valor por producto
        valor_total += i['precio'] * i['cantidad']
        
        # Se suman todas las cantidades
        cantidad_total += i['cantidad']
    
    # max busca el valor máximo en una lista
    # key=lambda x: x['precio'] indica que compare por precio
    mas_caro = max(inventario, key=lambda x: x['precio'])
    
    # Igual pero comparando por cantidad
    mayor_stock = max(inventario, key=lambda x: x['cantidad'])
    
    # return devuelve varios valores (en forma de tupla)
    return valor_total, cantidad_total, len(inventario), mas_caro, mayor_stock
