#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
s = int(input('Введите количество сделанных журавликов: '))
k = int((s/3)*2)
p = int((k/2)/2)
n = int(p)
print(p, k, n)