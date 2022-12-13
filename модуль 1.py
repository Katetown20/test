# задача 1
#name = input('Введите ваше имя: ')
#print('Hello,' + name)

# задача 2
#t1 = float(input('Введите температуру: '))
#t2 = t1 * 1.8 + 32
#print('Температура в Фарингейтах: ', t2)

# задача 3
#x1 = input('Введите число X1: ')
#x2 = input('Введите число X2: ')
#max1 = (x1 > x2) * x1 + (x2 >= x1) * x2
#print('Max: ', max1)

# задача 4
#print('Hello, my name is Shoppy. I am program for calculating the amount of purchases :)')
#p1 = int(input('Please, enter your first purchases: '))
#p2 = int(input('Please, enter your first purchases: '))
#p3 = int(input('Please, enter your first purchases: '))
#p4 = int(input('Please, enter your first purchases: '))
#p5 = int(input('Please, enter your first purchases: '))
#amount = p1 + p2 + p3 + p4 + p5
#print('Amount of  your purchases: ', amount)

# задача 5
#x1 = int(input('Введите позициь белого коня'))
#y1 = int(input('Введите позициь белого коня'))
#x2 = int(input('Введите позициь чёрного коня'))
#y2 = int(input('Введите позициь чёрного коня'))
#if (abs(x1 - x2) ==2) and (abs(y1 - y2) ==1):
#    print('Beaten')
#elif (abs(x1 - x2) ==1) and (abs(y1 - y2) ==2):
#    print('Beaten')
#else:
#    print('No!!!')

# задача 6
x = float(input('Enter dart position: '))
y = float(input('Enter dart position: '))

if x ** 2 + y ** 2 < 25:
    print('you have 100 game points')
elif x ** 2 + y ** 2 < 100:
    print('you have 50 game points')
elif x ** 2 + y ** 2 < 225:
    print('you have 20 game points')
else:
    print('you have 0 game points')
