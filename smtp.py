#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025


FROM = "oraffaudi@gmail.com"
TO = ["destino@server.com", "outro@server.com"]
SUBJECT = "Meu email via Python"
TEXT = """
Este é o meu email enviado pelo python
<b>Olá Mundo</b>
"""

mensagem = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""


with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, mensagem.encode("utf-8"))