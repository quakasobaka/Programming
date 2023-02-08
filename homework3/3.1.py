from random import randint
import math
new_list = []
for i in range(100):
    new_list.append(randint(1, 100))
print(new_list)
x = int(input("Введите искомое число от 1 до 100: "))
print(new_list.count(x))