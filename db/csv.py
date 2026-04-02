import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario está vacío. Nada que guardar.")
        return False
    
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            # Definimos las columnas basadas en las llaves de tu diccionario
            campos = ["id", "nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            if incluir_header:
                escritor.writeheader()
            
            escritor.writerows(inventario)
            print(f"[OK] Inventario guardado en: {ruta}")
            return True
    except (PermissionError, IOError) as e:
        print(f"Error de escritura: {e}")
        return False

def cargar_csv(ruta):
    productos_cargados = []
    errores = 0
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Validaciones y conversiones
                    id_prod = int(fila['id'])
                    nombre = fila['nombre']
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos")
                    
                    productos_cargados.append({
                        "id": id_prod,
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except (ValueError, KeyError):
                    errores += 1
                    
        return productos_cargados, errores
    except FileNotFoundError:
        print("[!] Archivo no encontrado.")
    except Exception as e:
        print(f"[!] Error inesperado: {e}")
    
    return None, errores
