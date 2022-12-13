# задача 1
value = (7*5/8+5)/3**5
print('Значение вырадения: ', value)

# задача 2
# S = v * t
v = int(input('Введите скорость: '))
t = int(input('Введите время: '))
way = 109
s = v*t
if s > way:
    s = s - way
print(s)

# задача 3
a = input('Введите число a: ')
b = input('Введите число b: ')
Max = (a >= b)*a or (b >= a)*b
print(Max)
print(Max)