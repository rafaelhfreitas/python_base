#!/usr/bin/env python3
"""Hello world multi linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Rafael Freitas"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("hello.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        print(f"You need use `=` in argument.")
        print(f"{str(e)}")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")


current_language = current_language[:5]

dictionarie ={
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, mondo!",
    "es_SP": "Hola, mundo!",
    "fr_FR": "Bonjour, monde!",
    "en_US": "Hello, world",
}
"""
message = dictionarie.get(current_language, dictionarie["en_US"])
"""

try:
    message = dictionarie[current_language]
except KeyError as e:
    log.error(
        "You need to use `=`, you passed %s, try --key=value: %s",
        arg,
        str(e)
    )
    sys.exit(1)

print(
    message * int(arguments["count"])
)


# if current_language == "pt_BR":
#     msg = "Olá, mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour, Monde!"
#print(msg)
