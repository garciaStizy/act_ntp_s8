import pandas as pd

def analizar_calificaciones():
    # Crear la Serie con índices personalizados
    calificaciones = pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])
    
    # Acceder a un valor específico por índice
    nota_ciencias = calificaciones['Ciencias']
    
    # Mostrar información básica de la Serie
    print("📚 Calificaciones por materia:")
    print(calificaciones)
    
    print("\n🔍 Nota en Ciencias:", nota_ciencias)
    
    # Calcular estadísticas básicas
    suma = calificaciones.sum()
    promedio = calificaciones.mean()
    
    print("\n Suma total de calificaciones:", suma)
    print(" Promedio de calificaciones:", promedio)

# Ejecutar la función
analizar_calificaciones()
