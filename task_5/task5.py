# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

num = int(input('Введите число:  '))
def fibb(num):
    lst = []
    f1, f2 = 1, 1
    for i in range(abs(num)):
        lst.append(f1)
        f1, f2 = f2, f1 + f2
    return lst
     
def neg_fibb(num):
    lst = []
    f1, f2 = 1, -1
    for i in range(abs(num)):
        lst.append(f1)
        f1, f2 = f2, (f1 + 1) - (f2 + 1)
    return lst

print(neg_fibb(num)[::-1] + [0] + fibb(num))


