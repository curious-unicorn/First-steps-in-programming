from math import pi

type_of_figure = str(input())
area = 0

if type_of_figure == 'square':
    a = float(input())
    area = a ** 2
elif type_of_figure == 'rectangle':
    a, b = float(input()), float(input())
    area = a * b
elif type_of_figure == 'circle':
    r = float(input())
    area = pi * r ** 2
elif type_of_figure == 'triangle':
    a, h = float(input()), float(input())
    area = (a * h) / 2
print(f"{area:.3f}")
