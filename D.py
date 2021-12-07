a = float(input('Число a: '))
b = float(input('Число b: '))
c = float(input('Число c: '))

D = b * b - (4 * a * c)

print('D =', D)

if D < 0:
    print('Корней нет')
elif D == 0:
    y = -b / (2 * a)
    print('x =', y)
else:
    x1 = (-b + (D ** 0.5)) / (2 * a)
    x2 = (-b - (D ** 0.5)) / (2 * a)
    print('x1 =', x1)
    print('x2 =', x2)