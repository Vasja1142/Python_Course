# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

X1 = int(input("Введите значение Х первой точки: "))
Y1 = int(input("Введите значение Y первой точки: "))
X2 = int(input("Введите значение Х второй точки: "))
Y2 = int(input("Введите значение Y второй точки: "))
result = ((X1 - X2)**2 + (Y1 - Y2)**2)**0.5
print(f"Расстояние между этими точками: {round(result, 2)}")