"""
This module is just for anotations
"""

# definition or assignment
# assignment
# documentation / docstring


def function_name(a: int, b: int, c: int) -> int:
    """This function do something with a, b and c.
    
    Use this function whem you want a + b + c

    :param a: Number
    :type a: int
    :param b: Number
    :type b: int    
    :param c: Number
    :type c: int    
    :return: Return the result of a + b + c
    :rtype: int


    >>> function_name(1,2,3)
    6
    """
    result = a + b + c
    return result

# positionals args
value = function_name(5,8,9)

# named args
value = function_name(a = 5, b =5, c =5)

# mixed args
value = function_name(5, c = 2, b = 3)

print(value)    



###########################

def another_function(a, b, c):
    """Explain what it does"""
    return a*2, b*2, c*2


another_value = another_function(1,2,3)
value1, value2,value3 = another_function(2,4,6)
print(another_value)    
print(value1, value2, value3)
value1, *_ = another_function(2,4,6)
print(value1)

value1, *rest = another_function(2,4,6)
print(rest)



###########################


# Passing args with unpacking

def sum(n1, n2):
    """ Does the sum of two numbers"""
    return n1 + n2

print(sum(5,1))

args = (7,3) 
print(sum(args[0], args[1]))
print(sum(*args))


args = {
    "n2": 70,
    "n1": 30
}

print(sum(n1 = args["n1"], n2 = args["n2"]))
print(sum(**args))


list_values_to_sum = [
    {"n1": 100, "n2": 200},
    {"n1": 100, "n2": 500},
    {"n1": 100, "n2": 700},
    (5, 10),
    [8, 13],
]


for item in list_values_to_sum:
    if isinstance(item, dict):
        print(sum(**item))
    else:
        print(sum(*item))