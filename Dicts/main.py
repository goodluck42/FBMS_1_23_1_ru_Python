# def get_names():
#     with open("name.txt", "r") as f:
#         name = "".join(f.readlines())
#
#     return name
#
# value = get_names()
#
# print(value)
import uuid

## global keyword

# value = 42


# def change():
#     global value
#
#     value = 10
#
#     print(value)
#
#
# change()
#
# print(value)

## tuples


# def get_user_data():
#     return "Alex", 23
#
#
# my_tuple = get_user_data()
#
# print(my_tuple)
# print(type(my_tuple))


## args
# def my_sum(*args):
#     for item in args:
#         print(item)
#
#
# with open("name.txt", "r") as f:
#     numbers = [int(value) for value in "".join(f.readlines()).split('\n')]
#
# print(f"numbers from file: {numbers}")
#
#
# # my_sum(numbers)  # my_sum([90, 10, 5, 60])
# my_sum(*numbers)  # my_sum(90, 10, 5, 60)


## coins, crystals, first name, last name, id
## tuple variant
# student = (100, 100, "Расул", "Умуд", str(uuid.uuid4()))
#
# print(f"COINS: {student[0]}")
# print(f"DIAMONDS: {student[1]}")
# print(f"NAME: {student[2]}")
# print(f"SURNAME: {student[3]}")
# print(f"ID: {student[4]}")
## dict
# student = {
#     "coins": 120,
#     "diamonds": 120,
#     "name": "Расул",
#     "surname": "Умуд",
#     "_id": str(uuid.uuid4()),  # генерация id
#     "grades": [12, 12, 12, 12, 10, 12]
# }

# values = student.values()
# keys = student.keys()
#
# for key in keys:
#     print(key)
#
# print('-' * 10)
#
# for value in values:
#     print(value)


def print_student(student: dict):
    for k, v in student.items():
        print(f"{k}: {v}")


def input_student():
    student = {}

    student["coins"] = int(input("Enter coins: "))
    student["diamonds"] = int(input("Enter diamonds: "))
    student["name"] = input("Enter name: ")
    student["surname"] = input("Enter surname: ")
    student["_id"] = str(uuid.uuid4())

    return student


student = input_student()

print_student(student)