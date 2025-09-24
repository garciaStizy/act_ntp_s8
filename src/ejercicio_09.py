import numpy as np
import pandas as pd

def dataframe_desde_numpy():
    # Crear un array NumPy 2D con datos de ventas trimestrales
    ventas_trimestrales = np.array([
        [12000, 13500, 15000],
        [9500, 10200, 11000],
        [18000, 17500, 19000]
    ])
    
    # Crear el DataFrame con nombres de columnas
    df = pd.DataFrame(ventas_trimestrales, columns=['Q1', 'Q2', 'Q3'])
    
    # Mostrar el DataFrame
    print("📊 DataFrame de ventas trimestrales:")
    print(df)
    
    # Verificar los tipos de datos
    print("\n🔍 Tipos de datos por columna:")
    print(df.dtypes)

# Ejecutar la función
dataframe_desde_numpy()
