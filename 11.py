def calculator():
    while True:
        try:
            expression = input("Введіть вираз для обчислення (наприклад 5 / 5):")
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Помилка: {e}")
        continue_calculation = input("Бажаєте продовжити?(y/так , n/ні): ").strip().lower()
        if continue_calculation not in ["yes", "y"]:
            print("Приходьте ще!")
            break
calculator()
...
