
class Rotor:
    def __init__(self, wiring, notch='Z', position='A'):
        self.wiring = wiring.upper()
        self.notch = ord(notch.upper()) - ord('A')
        self.position = ord(position.upper()) - ord('A')

    def get_position(self):
        return chr(self.position + ord('A'))

if __name__ == "__main__":
    rotor = Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("Rotor creado en posicion", rotor.get_position())
