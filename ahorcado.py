import random

# Lista de palabras
palabras = ["jirafa", "elefante", "murcielago", "computadora", "python", "samba"]

# Dibujo del ahorcado
ahorcado = [
    """
     ------
     |    |
     |    
     |   
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
    _|_
    """
]

def jugar():
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6
    letras_usadas = []

    while intentos >= 0:
        print(ahorcado[6 - intentos])
        palabra_mostrada = "".join([letra if letra in letras_adivinadas else "-" for letra in palabra])
        print(f"\nPalabra: {palabra_mostrada}")
        print("Letras ya dichas:", "".join(sorted(letras_usadas)))

        if "-" not in palabra_mostrada:
            print("¡Felicidades! Adivinaste la palabra.")
            break

        letra = input("Ingresa una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, ingresa una sola letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya dijiste esa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            letras_adivinadas.append(letra)
        else:
            intentos -= 1

    if intentos < 0:
        print(ahorcado[6])
        print(f"\nPerdiste... La palabra era: {palabra}")

def main():
    while True:
        jugar()
        continuar = input("\n¿Jugar de nuevo? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
