import csv
import pandas as pd

def gestionar_csv_cursos():
    nombre_archivo = 'cursos.csv'
    
    # Paso 1: Crear y escribir el archivo CSV
    cursos = [
        ['curso', 'instructor', 'duracion'],
        ['Python Básico', 'Laura Martínez', '4 semanas'],
        ['Análisis de Datos', 'Carlos Pérez', '6 semanas'],
        ['Machine Learning', 'Ana Torres', '8 semanas']
    ]
    
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(cursos)
        print("✅ Archivo CSV creado exitosamente.")
    except Exception as e:
        print("❌ Error al crear el archivo CSV:", e)
        return
    
    # Paso 2: Leer el archivo CSV con Pandas
    try:
        df = pd.read_csv(nombre_archivo)
        print("\n📘 DataFrame de cursos:")
        print(df)
    except FileNotFoundError:
        print("⚠️ El archivo no fue encontrado.")
    except Exception as e:
        print("❌ Error al leer el archivo CSV:", e)

# Ejecutar la función
gestionar_csv_cursos()
