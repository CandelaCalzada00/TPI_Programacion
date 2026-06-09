import os

def cargar_datos_csv(nombre_archivo):
    """
    Tarea 1: Leer el archivo CSV y carga los países en una lista de diccionarios.
    """
    lista_paises = []
    
    # Validamos si el archivo realmente existe en la carpeta para evitar que el programa se rompa
    if not os.path.exists(nombre_archivo):
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en esta carpeta.")
        return lista_paises

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # Descartamos la primera línea de encabezados
        archivo.readline()
        
        for linea in archivo:
            # Limpiamos espacios y separamos por comas
            datos = linea.strip().split(',')
            
            # Control de formato: Aseguramos que la línea tenga exactamente 4 datos
            if len(datos) == 4:
                try:
                    nuevo_pais = {
                        "nombre": datos[0].strip(),
                        "poblacion": int(datos[1].strip()),   # Conversión obligatoria a entero
                        "superficie": int(datos[2].strip()),  # Conversión obligatoria a entero
                        "continente": datos[3].strip()
                    }
                    lista_paises.append(nuevo_pais)
                except ValueError:
                    # Si población o superficie no son números, salta este registro sin romper el programa
                    print(f"Error de formato en la línea: {linea.strip()} (Datos numéricos inválidos)")
                    
    print(f"Se cargaron correctamente {len(lista_paises)} países.")
    return lista_paises

