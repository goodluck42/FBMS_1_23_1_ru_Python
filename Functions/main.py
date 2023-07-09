# students = []
#
#
# def add_student(student):  # student - это параметр
#     student = student.title()
#     students.append(student)
#
#
# def remove_student(student):
#     if student in students:
#         students.remove(student)
#
#
# def get_student_by_name(name):
#     name = name.lower()
#     for student in students:
#         if student.split(' ')[1].lower() == name:
#             return student
#
#
# def add(a, b):
#     result = a + b
#
#     return result
#
#
# def check_int(number):
#     if number > 0:
#         return 1
#     elif number < 0:
#         return -1
#     else:
#         return 0
#
#
# res = add(10, 42)
#
# print(res)
#
# result = check_int(42)
#
# print(result)
#
# # print(text)
#
# # text = input()
#
# # CRUD
# # C - CREATE
# # R - READ
# # U - UPDATE
# # D - DELETE
#
#
# add_student("Гасратова Ниса")
# add_student("Шукюров Кянан")
# add_student("Ашурбеков Осман")
# add_student("Эйвазова Медина")
# add_student("Исмайилбейли Фуад")
#
# # remove_student("Vadim")
#
# stud = get_student_by_name("ОсМаН")
#
# print(stud)
#


def add(a, b):
    result = a + b

    return result


num1 = int(input())
num2 = int(input())

res = add(num1, num2)

print(res)


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return not is_even(num)  # num % 2 != 0
