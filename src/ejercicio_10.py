import requests
import pandas as pd

def obtener_usuarios_api():
    url = "https://playground.mockoon.com/users"
    
    try:
        # Realizar la petición GET
        response = requests.get(url)
        
        # Verificar el código de estado
        if response.status_code == 200:
            print("✅ Conexión exitosa. Código de estado:", response.status_code)
            
            # Convertir la respuesta JSON a DataFrame
            df = pd.DataFrame(response.json())
            
            # Mostrar las primeras 5 filas
            print("\n👥 Primeras 5 filas del DataFrame:")
            print(df.head())
            
            # Mostrar información del DataFrame
            print("\n ℹInformación del DataFrame:")
            print(df.info())
        else:
            print(f"⚠️ Error en la respuesta. Código de estado: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(" Error de conexión con la API:", e)

# Ejecutar la función
obtener_usuarios_api()
