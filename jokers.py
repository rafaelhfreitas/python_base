def sum(a, b):
    return a + b

sum(1,2)
sum(1, b=5)

def hello(name, last_name = "Sobrenome"):
    print(f"Hello {name}, {last_name}")    


hello("Rafael", "Freitas")
hello("Rafael")


def function(*args, timeout=90, **kwargs):
    print(kwargs)
    print(args)

function("Rafael", 1, True, {}, [], timeout=50, name="Rafael", last_name="Freitas")
