

op = '0'
while True:
	numero = int(input("inserta un número: "))
	factorial = 1
	if numero ==0 or numero==1:
		print("El resultado es 1")

	elif numero<0:
		print("No es posible calcular el factorial de un número negativo")
	else:
		for i in range(1,numero + 1):
			factorial *=i
		print("El resultado del factorial de: ", numero, "es: ", factorial)
	op = input("Inserta una tecla para continuar o 0 para salir: ")
	if op == '0':
		print("Finalizar programa. Adiós!")
		break

	#try:
	#	numero = int(op)
	#except ValueError:
	#	print("Por favor, ingresa un número válido.")
