class MaxStudentsError(Exception):
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} років, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} років, {self.gender}, Залікова книжка: {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise MaxStudentsError("Неможливо додати більше 10 студентів до групи")
        self.group.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група номер:{self.number}\n{all_students}'


# Приклади використання
st1 = Student('Чоловік', 30, 'Гена', 'Вал', 'AN142')
st2 = Student('Жінка', 25, 'Ліза', 'Машина', 'AN145')
st3 = Student('Чоловік', 22, 'Саша', 'Чех', 'AN143')
st4 = Student('Чоловік', 20, 'Марк', 'Гел', 'AN144')
st5 = Student('Жінка', 21, 'Гана', 'Лера', 'AN146')
st6 = Student('Чоловік', 28, 'Сеня', 'Лис', 'AN147')
st7 = Student('Жінка', 24, 'Олена', 'Махич', 'AN148')
st8 = Student('Чоловік', 23, 'Іван', 'Сідоров', 'AN149')
st9 = Student('Жінка', 26, 'Аба', 'Гоп', 'AN150')
st10 = Student('Чоловік', 19, 'Володимир', 'Великий', 'AN151')
st11 = Student('Чоловік', 30, 'Нікола', 'Тесла', 'AN152')

gr = Group('PD1')
students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]

# Додаємо 10 студентів
for student in students:
    gr.add_student(student)

print(gr)

# Спроба додати 11-го студента
try:
    gr.add_student(st11)
except MaxStudentsError as e:
    print(e)  # Очікуваний результат: Неможливо додати більше 10 студентів до групи
