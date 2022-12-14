def convert_upper(text):
    return  text.upper()


def convert_lower(text):
    return text.lower()


def division_by_2(number):
    return number // 2 


def do_something(value, func):
    print(f"Aplicando {func} em {value}")
    return func(value)


do_something(10,lambda number: number * 3)


names = ["Bruno", "Joao", "Bernardo", "Cintia", "Marcia", "Juca"]

print(sorted(names, key=len))

print(sorted(names, key=lambda text: text.count("i")))

print(list(reversed(sorted(names, key=lambda text: text.count("i")))))

print(list(filter(lambda name: name[0].lower() == "b", names)))


print(list(map(lambda name: "Hello " + name, names)))


# operation = input("Operation: [sum, mul, div, sub]:").strip()
# n1 = int(input("n1:").strip())
# n2 = int(input("n2:").strip())

# operations = {
#     "sum": lambda a, b: a + b,
#     "mul": lambda a, b: a * b,
#     "div": lambda a, b: a // b,
#     "sub": lambda a, b: a - b,
# }


# print(f"O resultado é: {operations[operation](n1,n2)}")


(lambda: 1 + 1)()

(lambda a: a + 10)(1)