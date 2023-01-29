# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите 3-х значное число: "))
summary = 0
while number>0:
    summary = summary + number%10
    number //=10
    print(number)

print(summary)
    