import pandas as pd

def analizar_ventas_diarias():
    # Crear la Serie con ventas diarias
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165], 
                       index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    
    # Acceder al valor del índice 3
    valor_indice_3 = ventas[3]
    
    # Calcular el promedio de ventas
    promedio_ventas = ventas.mean()
    
    # Ordenar por valores
    ventas_ordenadas = ventas.sort_values()
    
    # Mostrar resultados
    print(" Ventas diarias:")
    print(ventas)
    print("\n Valor en el índice 3 (Jueves):", valor_indice_3)
    print("\n Promedio de ventas:", promedio_ventas)
    print("\n Ventas ordenadas de menor a mayor:")
    print(ventas_ordenadas)

# Ejecutar la función
analizar_ventas_diarias()
