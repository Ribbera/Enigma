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


def pedir_posiciones():
   #pide las 3 letras de las ventanillas hasta que sean validas
    while True:
        ventanas = input("Introduce 3 letras iniciales (ej: ABC): ").upper()
        if len(ventanas) == 3 and ventanas.isalpha():
            return ventanas
        print("Tienes que escribir exactamente 3 letras entre A y Z")

def cargar_rotores(ventanas):
    
    #carga los tres rotores desde los archivos de texto 
    
    try:
        rotor1 = Rotor.from_file("Rotor1.txt", ventanas[0])
        rotor2 = Rotor.from_file("Rotor2.txt", ventanas[1])
        rotor3 = Rotor.from_file("Rotor3.txt", ventanas[2])
        print("Rotores listos en posiciones:", ventanas[0], ventanas[1], ventanas[2])
        return rotor1, rotor2, rotor3
    except Exception as error:
        print("No se pudieron cargar los rotores:", error)
        return None, None, None


def cifrar_mensaje():

    # pregunta un texto, lo normaliza y lo cifra pasando por los tres rotores.

    print("\n" + "=" * 50)
    print("CIFRAR MENSAJE")
    print("=" * 50)


    #pedimos las posciones inciales 
    ventanas = pedir_posiciones()
    
    #cargamos los rotores en sus variables correspondientes asigndas en cargar_rotores()
    rotor1, rotor2, rotor3 = cargar_rotores(ventanas)
    if not rotor1:
        return

    mensaje_original = input("Escribe el mensaje a cifrar: ")
    
    with open("Missatge.txt", "w", encoding="utf-8") as f:
        f.write(mensaje_original)
        
    mensaje_limpio = normalizar_texto(mensaje_original)
    print("Mensaje preparado para cifrar:", mensaje_limpio)

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
    #lee el archivo Xifrat.txt y lo pasa hacia atras por lo rotores
    
    print("\n" + "=" * 50)
    print("DESCIFRAR MENSAJE")
    print("=" * 50)
    
    ventanas = pedir_posiciones()

    rotor1, rotor2, rotor3 = cargar_rotores(ventanas)
    if not rotor1:
        return

    try:
        with open("Xifrat.txt", "r") as archivo:
            texto_cifrado = archivo.read().replace(" ", "")
    except FileNotFoundError:
        print("No encontre el archivo Xifrat.txt, primero cifra algo.")
        return

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
    
def editar_rotores():

    #permite reescribir cualquiera de los tres archivos de rotor
    
    print("\n" + "=" * 50)
    print("EDITAR ROTORES")
    print("=" * 50)
    print("1. Rotor1.txt")
    print("2. Rotor2.txt")
    print("3. Rotor3.txt")

    opcion = input("Elige 1, 2 o 3: ")
    if opcion not in ["1", "2", "3"]:
        print("Opcion invalida.")
        return

    archivo = f"Rotor{opcion}.txt"

    while True:
        wiring = input("Escribe el wiring (26 letras unicas A-Z): ").upper()
        if len(wiring) == 26:
            letras_ok = True
            for letra in wiring:
                if letra < "A" or letra > "Z" or wiring.count(letra) > 1:
                    letras_ok = False
                    break
            if letras_ok:
                break
        print("El wiring debe tener 26 letras sin repetir.")

    while True:
        notch = input("Escribe la letra del notch (A-Z): ").upper()
        if len(notch) == 1 and notch.isalpha():
            break
        print("Solo una letra por favor.")

    with open(archivo, "w") as archivo_rotor:
        archivo_rotor.write(wiring + "\n")
        archivo_rotor.write(notch + "\n")

    print("Rotor guardado en", archivo)


def mostrar_menu():
    print("\n" + "=" * 50)
    print("MAQUINA ENIGMA")
    print("=" * 50)
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")
    print("=" * 50)
    
def main():
    print("Simulador sencillo de la Enigma (solo rotores).")
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            cifrar_mensaje()
        elif opcion == "2":
            descifrar_mensaje()
        elif opcion == "3":
            editar_rotores()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida, prueba de nuevo.")

        input("\nPulsa ENTER para volver al menu...")

        
if __name__ == "__main__":
    main()
