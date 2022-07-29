#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista das crianças agrupadas por sala
que frequenta cada uma das atividades.
"""

__version__ = "0.1.0"

sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca),
]


for nome_atividade, alunos in atividades:
    atividade_sala_1 = []
    atividade_sala_2 = []
    for aluno in alunos:
        if aluno in sala1:
            atividade_sala_1.append(aluno)
        elif aluno in sala2:
            atividade_sala_2.append(aluno)

    print(f"Sala 1 / Atividade: {nome_atividade} / Alunos: {atividade_sala_1}")
    print(f"Sala 2 / Atividade: {nome_atividade} / Alunos: {atividade_sala_2}")
    print("-" * 30)

