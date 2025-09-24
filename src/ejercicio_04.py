import pandas as pd

def crear_dataframe_productos():
    # Crear el diccionario con datos de productos
    datos_productos = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet'],
        'Precio': [1200, 800, 450],
        'Categoria': ['Electrónica', 'Electrónica', 'Electrónica']
    }
    
    # Convertir el diccionario a DataFrame
    df = pd.DataFrame(datos_productos)
    
    # Mostrar el DataFrame completo
    print("📦 DataFrame de productos:")
    print(df)
    
    # Acceder a la columna 'Precio'
    print("\n💰 Columna de precios:")
    print(df['Precio'])
    
    # Mostrar información básica del DataFrame
    print("\nℹ️ Información del DataFrame:")
    print(df.info())

# Ejecutar la función
crear_dataframe_productos()
