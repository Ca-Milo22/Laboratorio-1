# Ejercicio: Calcula subtotal, descuento y total de una compra con valores fijos.
precio = 85000.0
cantidad = 3
porcentaje_descuento = 0.10

subtotal = precio * cantidad
descuento = subtotal * porcentaje_descuento
total = subtotal - descuento

print("Precio unitario: $", precio)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", descuento)
print("Total: $", total)
