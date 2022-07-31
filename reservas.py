#!/usr/bin/env python
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas
`reservas.txt`
# cliente, quarto, dias
Bruno,3,12
Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""

import sys
import logging

bookings = {}
rooms = {}

try:
    for line in open("reservas.txt"):
        booking_client_name, room_code, days = line.strip().split(",")
        bookings[int(room_code)] = {
            "name": booking_client_name,
            "days": int(days),
        }
except FileNotFoundError:
    logging.error("Arquivo reservas não existe")
    sys.exit(1)


try:
    for line in open("quartos.txt"):
        code, room_desc, price = line.strip().split(",")
        rooms[int(code)] = {
            "name": room_desc,
            "price": float(price),
            "available": False if int(code) in bookings else True,
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)


print("Reserva hotel pythonico")
print("-" * 40)
if len(bookings) == len(rooms):
    print("Hotel lotado")
    sys.exit(1)
name = input("Nome do cliente: ").strip()
print("Lista de quartos:")
for code, data in rooms.items():
    room_name = data["name"]
    price = data["price"]
    available = "⛔" if not data["available"] else "👍"
    # available = data["available"] and "👍" or "⛔"
    print(f"{code} - {room_name} - R$ {price:.2f} - {available}")

print("-" * 40)

try:
    room = int(input("Número do quarto: ").strip())
    if not rooms[room]["available"]:
        print(f"O quarto {room} está ocupado.")
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"Quarto {room} não existe.")
    sys.exit(1)

try:
    days = int(input("Quantos dias ?: ").strip())
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)

room_description = rooms[room]["name"]
room_price = rooms[room]["price"]
available = rooms[room]["available"]
booking_price = room_price * days

with open("reservas.txt", "a") as file_:
    file_.write(f"{name},{room},{days}\n")

print(f"{name} você escolheu o quarto {room_description} e vai custar: R$: {booking_price:.,2f}")
