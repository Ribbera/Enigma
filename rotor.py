
class Rotor:
    def __init__(self, wiring, notch='Z', position='A'):
        wiring = wiring.upper()

        if len(wiring) != 26:
            raise ValueError("El wiring debe tener 26 letras")

        letras_vistas = []
        for letra in wiring:
            if letra < 'A' or letra > 'Z':
                raise ValueError("Solo letras A-Z")
            if letra in letras_vistas:
                raise ValueError("No se pueden repetir letras")
            letras_vistas.append(letra)

        self.wiring = wiring
        self.notch = ord(notch.upper()) - ord('A')
        self.position = ord(position.upper()) - ord('A')

    def avanzar(self):
        self.position += 1
        if self.position >= 26:
            self.position = 0

        if self.position == self.notch:
            return True
        return False

    def forward(self, letter):
        # Cifra letra
        letra = letter.upper()
        entrada_num = ord(letra) - ord('A')

        # Aplicar offset 
        entrada_con_pos = entrada_num + self.position
        while entrada_con_pos >= 26:
            entrada_con_pos -= 26

        letra_wiring = self.wiring[entrada_con_pos]
        salida_num = ord(letra_wiring) - ord('A')

        return chr(salida_num + ord('A'))

    def get_position(self):
        return chr(self.position + ord('A'))

if __name__ == "__main__":
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", "A")
    print("A ->", rotor.forward('A'))