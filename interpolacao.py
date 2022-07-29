#!/usr/bin/env python3
"""Imprime a mensagem de um e-mail

NÂO MANDE SPAM!!!
"""
__version__ = "0.1.0"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print(f"Informe o nome correto do arquivo !")
    sys.exit(1)

filename = arguments[0]
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, "email_tmpl.txt")

for line in open(filepath):
    name, email = line.split(",")
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)
