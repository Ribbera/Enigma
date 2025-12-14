# Máquina Enigma

Este es un simulador basico de la maquina Enigma que hemos hecho para la clase de Programación.

Permite cifrar mensajes de texto plano y tambien descifrarlos si ya estan encriptados. Ademas, se pueden configurar tres rotores con posiciones iniciales, y editar la configuracion de los rotores si hace falta.

## Descripción

Este proyecto implementa un simulador  de la máquina Enigma que permite:
- Cifrar mensajes de texto
- Descifrar mensajes cifrados
- Configurar 3 rotores con posiciones iniciales
- Editar la configuración de los rotores

## Archivos del proyecto

- `main.py`: Programa principal, con un menu interactivo para elegir que hacer.
- `rotor.py`: Clase Rotor que simula como gira y encripta un rotor individual.
- `Rotor1.txt`, `Rotor2.txt`, `Rotor3.txt`: Archivos de configuración de rotores.
- `Missatge.txt`: Mensaje original.
- `Xifrat.txt`: Mensaje cifrado.
- `Desxifrat.txt`: Mensaje descifrado.

## Cómo usar

```bash
python main.py
```

Después elige una opción del menú:
1. Cifrar mensaje
2. Descifrar mensaje
3. Editar rotores
4. Salir

## Requisitos

- Python 3.6 o superior
- No es necesario ningún requirments.txt
