#!/usr/bin/env python
"""Alerta de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:
temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
"ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."

"""
__version__ = "0.1.0"
__author__ = "Rafael Freitas"
__license__ = "Unlicense"

import sys
import logging
from typing import Dict

log = logging.Logger("alert")

arguments = {
    "temperatura": None,
    "umidade": None,
}

# TODO: Mover para modulo de utilidades

def is_completely_filled(dict_of_inputs: Dict) -> bool:
    """Returns a bool telling if a dict is completely filled"""
    arguments_size = len(dict_of_inputs)
    filled_size = len([value for value in dict_of_inputs.values() if value is not None])
    return arguments_size == filled_size 


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue

        try:
            dict_of_info[key] = float(input(f"Qual a {key} ?").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            break



while not is_completely_filled(arguments):
    read_inputs_for_dict(arguments)

# temp = arguments["temperatura"]
# umidade = arguments["umidade"]
temp, umidade = arguments.values()

if temp > 45:
    print("ALERTA !!!🥵 Perigo calor extremo")
elif temp * 3 >= umidade:
    print("ALERTA !!!🥵 ♒  Perigo calor úmido")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio")
elif temp < 0 :
    print("ALERTA !!!  ☃ Frio extremo")
