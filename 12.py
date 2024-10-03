import keyword
import string

def is_valid_variable_name(name):
    if keyword.iskeyword(name):
        return False
    if name[0].isdigit():
        return False
    if any(char.isupper() for char in name) or any(char in string.punctuation.replace('_', '') for char in name) or ' ' in name:
        return False
    if name.isidentifier():
        return True
    return False

input_string = "хочу відпустку"
print(is_valid_variable_name(input_string))
