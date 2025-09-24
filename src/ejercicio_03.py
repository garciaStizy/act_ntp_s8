import pandas as pd

def operaciones_con_series():
    # Crear las Series de precios y descuentos
    precios = pd.Series([100, 150, 200], index=['Producto A', 'Producto B', 'Producto C'])
    descuentos = pd.Series([10, 20, 15], index=['Producto A', 'Producto B', 'Producto C'])
    
    # Resta entre precios y descuentos
    precios_finales = precios - descuentos
    
    # Multiplicación por escalar (IVA del 16%)
    precios_con_iva = precios * 1.16
    
    # Mostrar resultados
    print("💰 Precios originales:")
    print(precios)
    
    print("\n🔻 Descuentos aplicados:")
    print(descuentos)
    
    print("\n🧾 Precios finales después de descuentos:")
    print(precios_finales)
    
    print("\n📈 Precios con IVA (16%):")
    print(precios_con_iva)
    
    print("\n✅ Operaciones elemento por elemento demostradas:")
    for producto in precios.index:
        print(f"{producto}: Precio {precios[producto]} - Descuento {descuentos[producto]} = {precios_finales[producto]} | con IVA: {precios[producto]} * 1.16 = {precios_con_iva[producto]:.2f}")

# Ejecutar la función
operaciones_con_series()
