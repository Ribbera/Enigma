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
        letra = letter.upper()
        entrada_num = ord(letra) - ord('A')

        entrada_con_pos = entrada_num + self.position
        while entrada_con_pos >= 26:
            entrada_con_pos -= 26

        letra_wiring = self.wiring[entrada_con_pos]
        salida_num = ord(letra_wiring) - ord('A')

        salida_final = salida_num - self.position
        while salida_final < 0:
            salida_final += 26

        return chr(salida_final + ord('A'))

    def reverse(self, letter):
        letra = letter.upper()
        entrada_num = ord(letra) - ord('A')

        entrada_con_pos = entrada_num + self.position
        while entrada_con_pos >= 26:
            entrada_con_pos -= 26

        letra_buscar = chr(ord('A') + entrada_con_pos)

        indice_en_wiring = -1
        indice = 0
        for letra_wiring in self.wiring:
            if letra_wiring == letra_buscar:
                indice_en_wiring = indice
                break
            indice += 1

        if indice_en_wiring == -1:
            raise ValueError("No se encontro la letra en el wiring")

        salida_num = indice_en_wiring - self.position
        while salida_num < 0:
            salida_num += 26

        return chr(salida_num + ord('A'))

    def get_position(self):
        return chr(self.position + ord('A'))