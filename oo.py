class Cor:
    def __str__(self):
        return self.icon

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()

class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


print("Cores secundárias")
print(Amarelo() + Vermelho())
print(Azul() + Amarelo())
print(Vermelho() + Azul())


class Paleta:

    def __init__(self, *cores):
        self._cores = cores

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._cores[item]
        elif isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())
for cor in rgb:
    print(cor, end="")

# print(rgb)
print(rgb[0])
print(rgb["azul"])
print(len(rgb))


"""

__new__              # Construtor chamado antes de criar a intância
__init__             # Inicializador chamado após a instância é criada
__init_subclass__    # Inicializador de subclasses
__repr__             # Imprime a representação em string
__str__              # chama __repr__ por padrão
__setattr__          # executado sempre que atribuimos com obj.name = value
__getattr__          # executado quando acessamos obj.name
__delattr__          # executado quando apagamos com `del obj.name`
__getattribute__     # executado quando um atributo não é encontrado
__dir__              # lista todos os atributos e métodos

"""