a = int(input("Введіть число a (1-1000): "))
b = int(input("Введіть число b (1-1000): "))

maximum = (a + b + abs(a - b)) // 2

print("Найбільше число:", maximum)
