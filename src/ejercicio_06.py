import pandas as pd

def crear_dataframe_libros():
    # Lista de listas: cada sublista representa un libro
    datos_libros = [
        ['Cien años de soledad', 'Gabriel García Márquez', 1967],
        ['1984', 'George Orwell', 1949],
        ['El nombre de la rosa', 'Umberto Eco', 1980]
    ]
    
    # Definir nombres de las columnas
    nombres_columnas = ['Titulo', 'Autor', 'Año']
    
    # Crear el DataFrame
    df = pd.DataFrame(datos_libros, columns=nombres_columnas)
    
    # Mostrar el DataFrame
    print("📖 DataFrame de libros:")
    print(df)
    
    # Mostrar las dimensiones del DataFrame
    print("\n📐 Dimensiones del DataFrame (filas, columnas):", df.shape)

# Ejecutar la función
crear_dataframe_libros()
