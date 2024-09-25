number1 = float(input("перше число: "))
operation = input("введить (+, /, *, -): ")
number2 = float(input("друге число: "))
if operation == "+":
    result = number1 + number2
    print(f"результат: {number1} + {number2} = {result}")
elif operation == "-":
    result = number1 - number2
    print(f"результат: {number1} - {number2} = {result}")
elif operation == "*":
    result = number1 * number2
    print(f"результат: {number1} * {number2} = {result}")
elif operation == "/":
    if number2 == 0:
        print("Error: делить на ноль нельзя!")
    else:
        result = number1 / number2
        print(f"результат: {number1} / {number2} = {result}")
else:
    print("Error :")
...
