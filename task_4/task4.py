#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input('Введите число : '))
def binary(n):
    b = ''
    while n > 0:
        b= str(n%2) + b
        n = n//2
    return int(b)
print(binary(n))