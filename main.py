
def normalizar_texto(texto):
    # Quitar acentos y dejar solo letras
    limpio = ""
    for letra in texto:
        if letra.isalpha():
            limpio += letra.upper()
    return limpio

def main():
    print("Probando normalizacion de texto")
    mensaje = input("Escribe algo: ")
    resultado = normalizar_texto(mensaje)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
