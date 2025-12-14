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

def agrupar_5(texto):
    grupos = []
    bloque = ""
    for letra in texto:
        bloque += letra
        if len(bloque) == 5:
            grupos.append(bloque)
            bloque = ""
    if bloque:
        grupos.append(bloque)
    return " ".join(grupos)

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

    #guardar  el cifrado en el archivo
    texto_formateado = agrupar_5(mensaje_cifrado)
    with open("Xifrat.txt", "w") as f:
        f.write(texto_formateado)

    # mostrar el texto cifrado con el formato correcto 
    print("Cifrado guardado en Xifrat.txt:", texto_formateado)
    

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
        paso = rotor1.reverse(paso)  
        mensaje_descifrado += paso

    #Guardar descifrado 
    with open("Desxifrat.txt", "w") as f:
        f.write(mensaje_descifrado)

     # mostrar el texto DEScifrado con el formato correcto 
    print("Descifrado guardado en Desxifrat.txt:", mensaje_descifrado)
    
def main():
    opcion = input("1=Cifrar, 2=Descifrar: ")
    if opcion == "1":
        cifrar_mensaje()
    elif opcion == "2":
        descifrar_mensaje()
        
if __name__ == "__main__":
    main()