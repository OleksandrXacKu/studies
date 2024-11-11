from student import Student
from group import Group

st1 = Student('Чоловік', 30, 'Гена', 'Вал', 'AN142')
st2 = Student('Жінка', 25, 'Ліза', 'Машина', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)
assert gr.find_student('Вал') == st1  # 'Гена Вал'
assert gr.find_student('Вал2') is None

gr.delete_student('Машина')
print(gr)  # Only one student
