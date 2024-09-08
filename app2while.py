import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 7

    print("He pensado en un número entre 1 y 100. ¡Intenta adivinarlo!")

    while intentos_restantes > 0:
        try:
            guess = int(input(f"Tienes {intentos_restantes} intentos restantes. Introduce tu adivinanza: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if guess < numero_secreto:
            print("El número es mayor que tu adivinanza.")
        elif guess > numero_secreto:
            print("El número es menor que tu adivinanza.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break

        intentos_restantes -= 1

    if intentos_restantes == 0:
        print(f"Se te han acabado los intentos. El número secreto era {numero_secreto}.")

# Llamar a la función para jugar
adivinar_numero()