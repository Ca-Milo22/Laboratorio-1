nombre = input("Nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
valor_por_hora = float(input("Valor por hora: "))

pago_total = horas * valor_por_hora

print("-------------------------")
print("     RESUMEN DE PAGO")
print("-------------------------")
print(f"Trabajador: {nombre}")
print(f"Horas: {horas}")
print(f"Valor por hora: ${valor_por_hora}")
print(f"Pago total: ${pago_total}")