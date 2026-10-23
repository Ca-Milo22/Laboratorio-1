# Ejercicio: Pide dos números y muestra las operaciones aritméticas básicas.
numero_1 = int(input("Primer número: "))
numero_2 = int(input("Segundo número: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
division_entera = numero_1 // numero_2
residuo = numero_1 % numero_2

print("-------------------------")
print("       RESULTADOS")
print("-------------------------")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Residuo:", residuo)