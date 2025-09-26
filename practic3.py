user_input = input("Введіть 4-значне число: ")

if user_input.isdigit() and len(user_input) == 4:
    digits_sum = sum(int(digit) for digit in user_input)
    print(" + ".join(user_input), "=", digits_sum)
else:
    print("Потрібно ввести саме 4-значне число.")
