# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии
def requrse(a, b):
    if (b == 1):
        return b
    if (b != 1):
        return (a * requrse(a, b - 1))

a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print(requrse(a,b))