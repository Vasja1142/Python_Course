# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

num = float(input('Введите любое дробное число: '))
num2 = int((num % 1) * 10)
print(num2)
