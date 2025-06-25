# 1. Crear el diccionario producto
producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}

# 2. Imprimir nombre y precio del producto
print(f"Producto: {producto['nombre']}, Precio unitario: ${producto['precio_unitario']}")

# 3. Simular una venta, restar 5 unidades al stock
producto["stock"] -= 5

# 4. Añadir clave "en_oferta" con valor True
producto["en_oferta"] = True

# 5. Imprimir el diccionario completo para ver los cambios
print(producto)