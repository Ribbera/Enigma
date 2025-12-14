# Maquina Enigma

Simulador simplificado de la máquina Enigma hecho para la clase de introducción a la programación. Permite cifrar y descifrar mensajes de texto y ajustar los tres rotores como en la máquina real. 

## Referencias
Basado en los videos de Coding Cassowary sobre la máquina Enigma y cifrado. 

## Descripcion rapida del codigo
- Normalización: el texto se pasa a mayúsculas, sin acentos ni símbolos, para trabajar solo con A-Z, y finalmente agrupando las letras en grupos de 5 separadas por un espacio.
- Rotores: cada letra atraviesa los tres rotores en orden; cada rotor avanza y arrastra al siguiente cuando toca el notch.
- Archivos: Missatge.txt guarda el mensaje original, Xifrat.txt el cifrado (en bloques de 5), Desxifrat.txt el descifrado.
- Configuración: los rotores se cargan desde Rotor1.txt, Rotor2.txt, Rotor3.txt; el menú permite editar wiring y notch.

## Archivos del proyecto
- `main.py`: menú interactivo y flujo principal.
- `rotor.py`: clase Rotor con giro, forward y reverse.
- `Rotor1.txt`, `Rotor2.txt`, `Rotor3.txt`: configuración de wiring y notch de cada rotor.
- `Missatge.txt`: mensaje original.
- `Xifrat.txt`: mensaje cifrado.
- `Desxifrat.txt`: mensaje descifrado.

## Cómo usar
```bash
python main.py
```
En el menú elige:
1. Cifrar mensaje
2. Descifrar mensaje
3. Editar rotores
4. Salir

## Requisitos
- Python 3.6 o superior
- No hace falta requirements.txt

## Nota sobre IA y buenas prácticas
- Antes de cada commit repasamos el código con ayuda de IA para aplicar buenas prácticas y mantenerlo limpio.
