# Ejercicio: Aplicación integradora: cotizador de compra con descuento e impuesto.
print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = float(input("Impuesto (%): "))

subtotal = precio_unitario * cantidad

print()
print("Subtotal:", subtotal)
descuento = porcentaje_descuento / 100
valor_descuento = subtotal * descuento

print("Descuento:", valor_descuento)

base = subtotal - valor_descuento

print("Base:", base)

impuesto = porcentaje_impuesto / 100
valor_impuesto = base * impuesto

print("Impuesto:", valor_impuesto)

total = base + valor_impuesto

print("Total:", total)

print()
print("-----------------------------")
print("      RESUMEN DE COMPRA")
print("-----------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"TOTAL: ${total}")