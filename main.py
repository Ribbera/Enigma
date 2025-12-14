import unicodedata
from rotor import Rotor

def normalizar_texto(texto):
    texto = unicodedata.normalize("NFD", texto)
    limpio = ""
    for caracter in texto:
        if unicodedata.category(caracter) == "Mn":
            continue
        letra = caracter.upper()
        if letra.isalpha():
            limpio += letra
    return limpio

def cifrar_mensaje():
    print("\nCIFRADO")

    #pedimos las posciones inciales 
    ventanas = input("3 letras iniciales (ej: ABC): ").upper()

    #cargamos los rotores en sus variables correspondientes
    rotor1 = Rotor.from_file("Rotor1.txt", ventanas[0])
    rotor2 = Rotor.from_file("Rotor2.txt", ventanas[1])
    rotor3 = Rotor.from_file("Rotor3.txt", ventanas[2])

    mensaje = input("Mensaje: ")
    mensaje_limpio = normalizar_texto(mensaje)

    mensaje_cifrado = ""
    for letra in mensaje_limpio:
        if rotor1.avanzar():
            if rotor2.avanzar():
                rotor3.avanzar()

        paso = rotor1.forward(letra)
        paso = rotor2.forward(paso)
        paso = rotor3.forward(paso)
        mensaje_cifrado += paso

    print("Cifrado:", mensaje_cifrado)

def descifrar_mensaje(texto_cifrado):
    print("\nDESCIFRADO")
    ventanas = input("3 letras iniciales: ").upper()

    rotor1 = Rotor.from_file("Rotor1.txt", ventanas[0])
    rotor2 = Rotor.from_file("Rotor2.txt", ventanas[1])
    rotor3 = Rotor.from_file("Rotor3.txt", ventanas[2])

    mensaje_descifrado = ""
    for letra in texto_cifrado:
        if rotor1.avanzar():
            if rotor2.avanzar():
                rotor3.avanzar()
    
        paso = rotor3.reverse(letra)
        paso = rotor2.reverse(paso)
        paso = rotor1.reverse(paso)  # <- linea corregida ahora usamos paso correctamente
        mensaje_descifrado += paso

    print("Descifrado:", mensaje_descifrado)
    
def main():
    cifrar_mensaje()

if __name__ == "__main__":
    main()