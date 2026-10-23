# Ejercicio: Genera una factura con subtotal, descuento, base, impuesto y total.
nombre_producto = "Teclado"
precio_unitario = 100000.0
cantidad = 2
porcentaje_descuento = 0.10

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento
base = subtotal - valor_descuento

porcentaje_impuesto = 0.19
valor_impuesto = base * porcentaje_impuesto
total = base + valor_impuesto

print("-------------------------")
print("     FACTURA SIMPLE")
print("-------------------------")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"Total: ${total}")