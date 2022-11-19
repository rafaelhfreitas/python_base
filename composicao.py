"""Print the names with starts with letter B"""

names = ["Rafael","Henrique", "Freitas", "Juliano", "Klicia", "Mayara", "Rodolfo"]

for name in names:
    if name.lower().startswith('r'):
        print(name)


# def starts_with_r(text):
#     #return text[0].lower() == 'r'
#     return text.startswith(('r', 'R'))

print(*list(filter(lambda text: text.startswith(('r', 'R')), names)), sep="\n")