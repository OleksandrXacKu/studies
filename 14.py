def format_time(seconds):
    if not (0 <= seconds < 864000):
        return "Число повинно бути більше або дорівнювати 0 і меньше ніж 8640000."

    SECONDS_IN_DAY = 24 * 60 * 60
    SECONDS_IN_HOUR = 60 * 60
    SECONDS_IN_MINUTE = 60

    days, remainder = divmod(seconds, SECONDS_IN_DAY)
    hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    return formatted_time

user_input = int(input("Введіть кількість секунд (0 <= секунд < 8640000): "))
result = format_time(user_input)
print(result)