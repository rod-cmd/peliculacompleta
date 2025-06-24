# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear tres diccionarios representando productos diferentes
producto1 = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}

producto2 = {
    "codigo": "P002",
    "nombre": "Café de los Yungas",
    "precio_unitario": 25.00,
    "stock": 100,
    "proveedor": "Café Yungueño S.A."
}

producto3 = {
    "codigo": "P003",
    "nombre": "Quinua Real en Grano",
    "precio_unitario": 12.75,
    "stock": 80,
    "proveedor": "Andes Naturales"
}

# 3. Añadir los productos a la lista inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir la cantidad de tipos de producto en el inventario
print(f"Cantidad de productos en el inventario: {len(inventario)}")

# 5. Recorrer la lista con un bucle for e imprimir el resumen
print("--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")