class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Cliente:
    def __init__(self, nombre, email, direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion

class Pedido:
    def __init__(self, id_pedido, cliente, productos):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = productos  
        self.estado = "Pendiente"

class TiendaOnline:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.pedidos = []
        self._inicializar_datos()

    def _inicializar_datos(self):
        # Agregar algunos productos iniciales
        self.productos.extend([
            Producto(1, "Camiseta", 19.99, 100),
            Producto(2, "Zapatos", 49.99, 50),
            Producto(3, "Gorra", 14.99, 200)
        ])

        # Agregar algunos clientes iniciales
        self.clientes.extend([
            Cliente("Juan Pérez", "juan@email.com", "Calle 123"),
            Cliente("María García", "maria@email.com", "Avenida 456")
        ])

        # Crear algunos pedidos iniciales
        cliente1 = self.clientes[0]
        pedido1 = Pedido(101, cliente1, [self.productos[0], self.productos[2]])
        self.pedidos.append(pedido1)

    def agregar_producto(self, nombre, precio, stock):
        nuevo_id = len(self.productos) + 1
        nuevo_producto = Producto(nuevo_id, nombre, precio, stock)
        self.productos.append(nuevo_producto)
        return nuevo_producto

    def actualizar_estado_pedido(self, id_pedido, nuevo_estado):
        for pedido in self.pedidos:
            if pedido.id_pedido == id_pedido:
                pedido.estado = nuevo_estado
                return True
        return False

    def buscar_pedidos_por_email(self, email):
        pedidos_cliente = []
        for pedido in self.pedidos:
            if pedido.cliente.email == email:
                pedidos_cliente.append(pedido)
        return pedidos_cliente

# Ejemplo de uso
if __name__ == "__main__":
    tienda = TiendaOnline()

    while True:
        print("\n=== MENÚ TIENDA ONLINE ===")
        print("1. Agregar nuevo producto")
        print("2. Actualizar estado de pedido")
        print("3. Buscar pedidos por email")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                
                nuevo_producto = tienda.agregar_producto(nombre, precio, stock)
                print(f"\nNuevo producto agregado: {nuevo_producto.nombre}")
                
            case "2":
                id_pedido = int(input("Ingrese el ID del pedido: "))
                nuevo_estado = input("Ingrese el nuevo estado del pedido: ")
                
                if tienda.actualizar_estado_pedido(id_pedido, nuevo_estado):
                    print("\nEstado del pedido actualizado exitosamente")
                else:
                    print("\nNo se encontró el pedido especificado")
                    
            case "3":
                email = input("Ingrese el email del cliente: ")
                pedidos = tienda.buscar_pedidos_por_email(email)
                
                print(f"\nPedidos encontrados: {len(pedidos)}")
                for pedido in pedidos:
                    print(f"ID: {pedido.id_pedido}, Estado: {pedido.estado}")
                    print("Productos:")
                    for producto in pedido.productos:
                        print(f"- {producto.nombre}: ${producto.precio}")
                    print()
                    
            case "4":
                print("\n¡Gracias por usar la Tienda Online!")
                break
                
            case _:
                print("\nOpción no válida. Por favor, intente nuevamente.")