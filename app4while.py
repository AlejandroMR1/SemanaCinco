def calculadora():
    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Salir")

        opcion = input("Selecciona una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        if opcion == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == '4':
            if num2 == 0:
                print("Error: División por cero no permitida.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

calculadora()
