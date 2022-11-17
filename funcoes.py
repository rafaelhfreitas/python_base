#!/usr/bin/env python3
""" Exemplo de funções """
"""
f(x) = 5 *x/2
"""
__version__ = "0.0.1"
__author__ = "Rafael Freitas"
__license__ = "Unlicense"


def f(x):
    return 5 * (x/2)

print(f(10))
print(f(10) == 25)


def double(x):
    return x * 2



def print_in_super(text):
    print(text.upper())


print_in_super('rafael')



def heron(a,b,c):
    """ Calcula a area de um triangulo não equilatero """
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s -b) * (s -c)
    return area**0.5

def heron2(params):
    return heron(*params)

area_triangulo = heron(3, 4 , 5)
print(area_triangulo)


triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35 ,37)
]

print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron2(t)
    print(f"A area do tringualo é: {area}")