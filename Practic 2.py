"""Завдання практичної №2. """

import math
from statistics import geometric_mean

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

sum = a + b
prod = a * b
diff = a - b
arithmetic = (a+b) / 2
geometric_mean = math.sqrt(abs(a * b))
distance = abs (a - b)
maximum = max (a, b)
minimum = min (a, b)
sum_square = a**2 + b**2
square_sum = (a + b)**2
power = a ** b

print(f"1. Сума: {sum}")
print(f"2. Різниця: {diff}")
print(f"3. Добуток: {prod}")
print(f"4. Середнє арифметичне: {arithmetic}")
print(f"5. Середнє геометричне: {geometric_mean}")
print(f"6. Відстань: {distance}")
print(f"7. Максимум: {maximum}")
print(f"8. Мінімум: {minimum}")
print(f"9. Сума квадратів: {sum_square}")
print(f"10. Квадрат суми: {square_sum}")
print(f"11. a в степені b: {power}")



