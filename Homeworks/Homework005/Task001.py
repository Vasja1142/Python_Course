# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.

import random
numbers = [random.randint(1, 10) for i in range(10)]
result = filter(lambda x: x > 5, numbers)
print(numbers)
print(list(result))