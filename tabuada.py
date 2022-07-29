#!/usr/bin/env python3
"""Script para impressão da tabuada de 1 a 10
Execução:

    python3 tabuada.py
    ou
    ./tabuada.py
"""
__version__ = "0.0.1"
__author__ = "Rafael Freitas"
__license__ = "Unlicense"


base = list(range(1, 11))
template = """

{bloco:^18}

##################    
"""

for n1 in base:
    print("{:-^18}".format("Tabuada do {n1}"))
    print()
    for n2 in base:
        resultado= n1 * n2
        print("{:^18}".format(f"{n1} X {n2} = {resultado}"))
    print("#" * 18)

# for number in base:
#     print("Tabuada do número: ", number)
#     for another_number in base:
#         print(another_number * number)
#     print("-" * 12)
