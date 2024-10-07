import string

def get_letters_between(start_end):
    letters = string.ascii_letters
    start_letter, end_letter = start_end.split('-')

    start_index = letters.index(start_letter)

    end_index = letters.index(end_letter)

    return letters[start_index:end_index + 1]

user_input = input("Введіть дві літери через дефіс (наприклад, a-e): ")
result = get_letters_between(user_input)
print(result)