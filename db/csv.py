import csv

# Esta función guarda el inventario en un archivo CSV
def guardar_csv(inventario, ruta):
    # Verifica si la lista está vacía
    if not inventario:
        print("Inventario vacío. Nada que guardar.")
        return
    
    try:
        # open abre el archivo
        # 'w' significa escribir (write)
        # newline evita líneas en blanco extra
        # encoding='utf-8' permite caracteres especiales
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            
            # fieldnames define las columnas del CSV
            campos = ["nombre", "precio", "cantidad"]
            
            # DictWriter permite escribir diccionarios en CSV
            writer = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribe la primera fila (encabezado)
            writer.writeheader()
            
            # Recorre cada producto
            for p in inventario:
                # writerow escribe una fila
                writer.writerow({
                    "nombre": p["nombre"],
                    "precio": p["precio"],
                    "cantidad": p["cantidad"]
                })
        
        print(f"Inventario guardado en: {ruta}")
    
    except Exception as e:
        # Si ocurre un error, lo muestra
        print(f"Error al guardar: {e}")


# Esta función carga un archivo CSV y valida los datos
def cargar_csv(ruta):
    productos = []
    errores = 0
    
    try:
        # 'r' significa leer (read)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            
            # DictReader convierte cada fila en diccionario
            reader = csv.DictReader(archivo)
            
            # Validar que el encabezado sea correcto
            if reader.fieldnames != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return None, 0
            
            # Recorre cada fila del archivo
            for fila in reader:
                try:
                    # Verifica que tenga 3 columnas
                    if len(fila) != 3:
                        raise ValueError
                    
                    # Convierte texto a número
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])  # convierte a decimal
                    cantidad = int(fila["cantidad"])  # convierte a entero
                    
                    # Validar que no sean negativos
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    # Guarda el producto válido
                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                
                except:
                    # Si algo falla, suma un error
                    errores += 1
        
        print(f"{errores} filas inválidas omitidas")
        
        # return devuelve dos valores: lista y cantidad de errores
        return productos, errores
    
    except FileNotFoundError:
        print("Archivo no encontrado")
    
    except:
        print("Error al cargar archivo")
    
    return None, errores