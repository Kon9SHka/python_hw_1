"""
Задача 8: Требуется определить, можно ли от шоколадки размером n x m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
"""
n = int(input("Введите длину шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Кол-во долек: "))

if (k%n==0 or k%m==0) and k <= m*n:
    print("У Вас получится разломить шоколадку за один раз")
else:
    print("Нужно сделать больше одного разлома или шоколадка слишком маленькая")