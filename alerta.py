#!usr/bin/env python3
"""
Faça um script que pergunta ao usuario qual a temperatura atual e o indice de
umidade do ar e exiba uma mensagem de alerta na tela dependedo das
condições informadas:

Temp maior que 45: ALERTA!! Perigo calor extremo
Temp vezes 3 for maior ou igual a umidade: ALERTA!! Perigo de calor úmido
Temp entre 10 e 30: Normal
Temp entre 0 e 10: Frio
Temp menor que 0: Frio extremo
"""

import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!! 🥵​ Perigo calor extremo.")
elif temp * 3 >= umidade:
    print("ALERTA!! 🥵💧 Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("👍 Normal")
elif temp >= 0 and temp <= 9:
    print("🧊 Frio")
elif temp < 0:
    print("ALERTA!! 🥶 Frio extremo")