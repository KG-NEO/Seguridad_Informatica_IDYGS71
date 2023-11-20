# PRODUCTOS EN VENTA
productos = {
    "Iphone 11": 1000.0,
    "MacBook Pro 2018": 7000.0,
    "Ipad Air 9 Gn": 5000.0,
    "Lenovo Tab": 2800.0,
}

# Lista de productos
def mostrar_productos():
    print("Lista de Productos:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio:.2f}")

# Función para calcular el total de la compra
def calcular_total(carrito):
    total = 0
    for producto, cantidad in carrito.items():
        if producto in productos:
            total += productos[producto] * cantidad
    return total

# Función principal de venta
def venta_de_productos():
    print("¡Bienvenido a la UT STORE!")

    carrito = {}
    continuar_comprando = True

    while continuar_comprando:
        mostrar_productos()
        producto = input("Ingrese el nombre del producto que desea comprar: ")
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))

        if producto in productos:
            if producto in carrito:
                carrito[producto] += cantidad
            else:
                carrito[producto] = cantidad
        else:
            print("Producto no válido. Por favor, elija un producto de la lista.")

        seguir = input("¿Desea seguir comprando? (si/no): ")
        if seguir.lower() != "si":
            continuar_comprando = False

    print("Resumen de la compra:")
    for producto, cantidad in carrito.items():
        print(f"{producto}: {cantidad} unidades")

    total = calcular_total(carrito)
    print(f"Total de la compra: ${total:.2f}")

