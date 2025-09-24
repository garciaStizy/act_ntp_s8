import pandas as pd

def crear_dataframe_empleados():
    # Crear la lista de diccionarios con datos de empleados
    lista_empleados = [
        {'empleado': 'Ana Gómez', 'salario': 3500, 'departamento': 'Finanzas'},
        {'empleado': 'Luis Torres', 'salario': 4200, 'departamento': 'Marketing'},
        {'empleado': 'Carlos Ruiz', 'salario': 3900, 'departamento': 'IT'}
    ]
    
    # Convertir la lista a DataFrame
    df = pd.DataFrame(lista_empleados)
    
    # Mostrar el DataFrame completo
    print("👥 DataFrame de empleados:")
    print(df)
    
    # Acceder a filas específicas usando índices
    print("\n🔍 Acceder a la segunda fila (índice 1):")
    print(df.iloc[1])
    
    print("\n🔍 Acceder a las dos primeras filas:")
    print(df.iloc[:2])

# Ejecutar la función
crear_dataframe_empleados()
