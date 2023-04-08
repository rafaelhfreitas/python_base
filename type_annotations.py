"""

name: str = 'Rafael'
number: int = 42
quantity: float = 56.3
active: bool = False


def sum(a: int, b: int ) -> int:
    return a + b


print(__annotations__)


print(sum.__annotations__)


from typing import Union

def sum(a: Union[int, float, str], b: Union[int, float, str]): 
    return a + b


"""
# from typing import Union, List, Any, Optional


# OptionalMessage = Optional[Union[int, str, List]]
# # Required python3.9>
# # OptinalMessage = int | float | list | None


# def print_message(msg: OptionalMessage = None) -> None:
#     print(msg)


# print_message('Rafael')
# print_message(123)
# print_message([1, 2, 3])


# from typing import Union


# def sum(a: Union[int,  str], b: Union[int,  str]) -> Union[int, str]:
#     return a + b


# sum(1,2)
# sum(5, 4)
# sum('Rafael', 'Rafael')

# from decimal import Decimal

# product = 'Pen'
# value = Decimal(4.5)
# quantity = 5
# especial_customer = True


# def calculate_total(value: Decimal, quantity: int) -> Decimal:
#     if not isinstance(value, Decimal):
#         raise ValueError('Type of value require Decimal')
#     return Decimal(value * quantity)


# if especial_customer:
#     value = Decimal(4.3)

# total = calculate_total(value, quantity)

# print('Type: ', type(value))
# print(f"The total is R${total:.2f}")


class Person:
    def __init__(self, pk: str, name: str, points: int):
        self.pk = pk
        self.name = name
        self.points = points


def function(data: Person):
    ...


dados = Person(pk="rafael@rafael.com", name="Rafael", points=100)

function(dados)