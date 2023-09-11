"""
Задания:
    1. Cоздайте экземпляр класса студенда.
    2. Получите его полное имя используя метод get_full_name.
    3. Положите результат вызова метода get_full_name в переменную и распечатайте ее.
"""


class Student:
    def __init__(self, name: str, surname: str, faculty: str, course: int) -> None:
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course

    def get_full_name(self):
        return f"Student's full name: {self.surname}, {self.name}"


if __name__ == '__main__':
    first_student = Student(name='Anna', surname='Petrova', faculty='singing', course=1)
    first_students_name = first_student.get_full_name()
    print(first_students_name)

