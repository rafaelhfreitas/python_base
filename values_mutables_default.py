# set, dict, list   = mutable 

s = set()
s.add(1)

l = []
l.append(1)

d = {}
d["key"] = "value"

def add_list(value, list = None):
    if list is None:
        list = []   
    list.append(value)
    return list


add_list(4),
add_list(5),
print(add_list(6))    