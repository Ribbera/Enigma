class Rotor:
    """
    Rotor basico: guarda el cableado (wiring), la posicion y el notch
    Todo se hace paso a paso para que sea facil de seguir.
    """
    

    def __init__(self, wiring, notch='Z', position='A'):
        wiring = wiring.upper()
        notch = notch.upper()
        position = position.upper()

        if len(wiring) != 26:
            raise ValueError("El wiring debe tener 26 letras en mayusculas.")

        # Revisamos letra a letra para evitar caracteres raros o repetidos.
        letras_vistas = []
        for letra in wiring:
            if letra < 'A' or letra > 'Z':
                raise ValueError("El wiring solo acepta letras A-Z.")
            if letra in letras_vistas:
                raise ValueError("El wiring no puede repetir letras.")
            letras_vistas.append(letra)

        if len(notch) != 1 or notch < 'A' or notch > 'Z':
            raise ValueError("El notch debe ser una letra A-Z.")

        if len(position) != 1 or position < 'A' or position > 'Z':
            raise ValueError("La posicion debe ser una letra A-Z.")

        self.wiring = wiring
        self.notch = ord(notch) - ord('A')
        self.position = ord(position) - ord('A')

    def avanzar(self):
      
        #Avanza una posicion. Devuelve True si toca mover el siguiente rotor.
       
        self.position += 1
        if self.position >= 26:
            self.position = 0

        if self.position == self.notch:
            return True
        return False

    def forward(self, letter):
        
       #Paso de cifrado: entra una letra y sale otra segun el wiring.
    
        letra = letter.upper()
        entrada_num = ord(letra) - ord('A')

        # Aplicamos el offset de la posicion actual.
        entrada_con_pos = entrada_num + self.position
        while entrada_con_pos >= 26:
            entrada_con_pos -= 26

        letra_wiring = self.wiring[entrada_con_pos]
        salida_num = ord(letra_wiring) - ord('A')

        # Quitamos el offset.
        salida_final = salida_num - self.position
        while salida_final < 0:
            salida_final += 26

        return chr(salida_final + ord('A'))

    def reverse(self, letter):
        
        #Paso de descifrado: buscamos la posicion de la letra en el wiring.
       
        letra = letter.upper()
        entrada_num = ord(letra) - ord('A')

        # Ajustamos con la posicion del rotor.
        entrada_con_pos = entrada_num + self.position
        while entrada_con_pos >= 26:
            entrada_con_pos -= 26

        letra_buscar = chr(ord('A') + entrada_con_pos)

        #Buscamos donde aparece esa letra en el wiring sin atajos raros.
        indice_en_wiring = -1
        indice = 0
        for letra_wiring in self.wiring:
            if letra_wiring == letra_buscar:
                indice_en_wiring = indice
                break
            indice += 1

        if indice_en_wiring == -1:
            raise ValueError("La letra no se encontro en el wiring.")

        salida_num = indice_en_wiring - self.position
        while salida_num < 0:
            salida_num += 26

        return chr(salida_num + ord('A'))

    def set_position(self, position):
        
        #Cambia la posicion del rotor.
       
        if isinstance(position, str):
            position = position.upper()
            self.position = ord(position) - ord('A')
        else:
            self.position = int(position) % 26

    def get_position(self):
        
        #Devuelve la posicion como letra.
        
        return chr(self.position + ord('A'))
    
# Con la ayuda de la ia nos ha desarollado esta sección ya que siguiendo el video tuvimos problemas.
    @classmethod
    def from_file(cls, filepath, position='A'):
      
        #Carga un rotor desde un archivo de texto (linea 1 wiring, linea 2 notch).
       
        try:
            with open(filepath, 'r') as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"No encontre el archivo {filepath}")

        if len(lineas) == 0:
            raise ValueError("El archivo del rotor esta vacio.")

        wiring = lineas[0].strip().upper()

        if len(lineas) > 1:
            notch = lineas[1].strip().upper()
        else:
            notch = 'Z'

        return cls(wiring, notch, position)
