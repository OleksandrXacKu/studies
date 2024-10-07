def multiply_digits_until_single_digit(n):
    while n > 9:
        result = 1
        for digit in str(n):
            result *= int(digit)
        n = result
    return n

user_input = int(input("Введіть ціле число: "))
result = multiply_digits_until_single_digit(user_input)
print(f"Результат: {result}")
...
