import json
import pandas as pd

def gestionar_json_vehiculos():
    nombre_archivo = 'vehiculos.json'
    
    # Paso 1: Crear la lista de objetos (diccionarios)
    lista_vehiculos = [
        {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2020},
        {'marca': 'Ford', 'modelo': 'Focus', 'año': 2018},
        {'marca': 'Honda', 'modelo': 'Civic', 'año': 2022}
    ]
    
    # Paso 2: Guardar el archivo JSON
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
            json.dump(lista_vehiculos, archivo_json, indent=4)
        print("✅ Archivo JSON guardado exitosamente.")
    except Exception as e:
        print("❌ Error al guardar el archivo JSON:", e)
        return
    
    # Paso 3: Leer el archivo JSON con Pandas
    try:
        df = pd.read_json(nombre_archivo)
        print("\n🚘 DataFrame de vehículos:")
        print(df)
        
        print("\n🔍 Tipos de datos por columna:")
        print(df.dtypes)
    except FileNotFoundError:
        print("⚠️ El archivo JSON no fue encontrado.")
    except Exception as e:
        print("❌ Error al leer el archivo JSON:", e)

# Ejecutar la función
gestionar_json_vehiculos()
