class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al carrito.
        El producto debe ser un diccionario con claves 'nombre' y 'precio'.
        """
        if isinstance(producto, dict) and "nombre" in producto and "precio" in producto:
            self.productos.append(producto)
        else:
            print("Producto inválido. Debe ser un diccionario con 'nombre' y 'precio'.")

    def calcular_total(self):
        """
        Calcula el total de todos los productos en el carrito.
        """
        total = sum(producto["precio"] for producto in self.productos)
        return total

    def mostrar_carrito(self):
        """
        Muestra todos los productos del carrito y el total.
        """
        if not self.productos:
            print("El carrito está vacío.")
            return

        print("Productos en el carrito:")
        for producto in self.productos:
            print(f"- {producto['nombre']}: ${producto['precio']:.2f}")
        total = self.calcular_total()
        print(f"Total a pagar: ${total:.2f}")
