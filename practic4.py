import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

if a == 0:
    print("Це не квадратне рівняння.")
else:
    d = b**2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Два корені: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Один корінь: x = {x:.2f}")
    else:
        print("Рівняння не має коренів")
