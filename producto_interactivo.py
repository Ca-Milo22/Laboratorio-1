# Ejercicio: Pide producto, precio y cantidad y calcula el subtotal.
producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad

print("Producto:", producto)
print("Subtotal: $", subtotal)