# Maquina Enigma

Simulador basico de la maquina Enigma hecho para clase de programacion. Permite cifrar y descifrar mensajes de texto y ajustar los tres rotores como en la maquina real.

## Descripcion rapida del codigo
- Normalizacion: el texto se pasa a mayusculas, sin acentos ni simbolos, para trabajar solo con A-Z, y finalmente agrupando las letras en grupos de 5 separadas por un espacio.
- Rotores: cada letra atraviesa los tres rotores en orden; cada rotor avanza y arrastra al siguiente cuando toca el notch.
- Archivos: `Missatge.txt` guarda el mensaje original, `Xifrat.txt` el cifrado (en bloques de 5), `Desxifrat.txt` el descifrado.
- Configuracion: los rotores se cargan desde `Rotor1.txt`, `Rotor2.txt`, `Rotor3.txt`; el menu permite editar wiring y notch.

## Archivos del proyecto
- `main.py`: menu interactivo y flujo principal.
- `rotor.py`: clase Rotor con giro, forward y reverse.
- `Rotor1.txt`, `Rotor2.txt`, `Rotor3.txt`: configuracion de wiring y notch de cada rotor.
- `Missatge.txt`: mensaje original.
- `Xifrat.txt`: mensaje cifrado.
- `Desxifrat.txt`: mensaje descifrado.

## Como usar
```bash
python main.py
```
En el menu elige:
1. Cifrar mensaje
2. Descifrar mensaje
3. Editar rotores
4. Salir

## Requisitos
- Python 3.6 o superior
- No hace falta requirements.txt

## Nota sobre IA y buenas practicas
- Antes de cada commit repasamos el codigo con ayuda de IA para aplicar buenas practicas y mantenerlo limpio.
