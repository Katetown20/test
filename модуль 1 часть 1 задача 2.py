# задача 2
# S = v * t
v = int(input('Введите скорость: '))
t = int(input('Введите время: '))
way = 109
s = v * t % way
print(s)
