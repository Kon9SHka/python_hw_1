"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, а 
Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""

count_birds = int(input("Введите общее кол-во журавликов, сделанных детьми: "))

print("Петя: " + str(count_birds/4))
print("Сережа: " + str(count_birds/4))
print("Катя: " + str(count_birds/2))