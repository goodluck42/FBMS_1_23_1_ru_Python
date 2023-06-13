# int, float, bool, char
# str, list

# a = 42
# b = "Hello python!"
#
# student1 = "Абдуллаев Мурад Ариф"
# student2 = "Алиев Вагиф Тогрул"
# # ...
# student16 = "Эйвазова Медина Намик"
######################################
#              0        1         2
# students = ["Мурад", "Вагиф", "Медина"]
#
# students[0] = "Эмиль"
# # students[0] = 6218736127836 ## Bad practice
#
# print(students)
# print(students[0])
###############################

#### SAMPLE1
# students = []
#
# while True:
# 	student = input("Enter student name: ")
#
# 	if student == "":
# 		break
#
# 	students.append(student)
#
# 	if len(students) == 3:
# 		print("Student limit exceeded")
# 		break
#
# print(students)
####################
#### len
# val = [1, 2, 90, 42, 0]
#
# length = len(val)
#
# print(length)

########
#### WHILE VARIANT
# students = ["Мурад", "Вагиф", "Медина"]
# i = 0
# count = len(students)  # count = 3
#
# while i < count:  # i < 3
# 	# 0 1 2
# 	print(f"{i + 1}. {students[i]}")
# 	i += 1

#### FOR VARIANT

# students = ["Мурад", "Вагиф", "Медина"]
#
# # my_range = range(1, 10)
#
# i = 1
#
# for student in students:
# 	print(f"{i}. {student}")
# 	i += 1

#########################
### list modifying
## BAD
# prices = [40, 42, 50, 60]
#
# for price in prices:
# 	price *= 0.9
#
# print(prices)
## WHILE VARIANT

# prices = [40, 42, 50, 60]
# i = 0
# length = len(prices)  # length = 4
#
# while i < length:  # i < 4
# 	# 0 1 2 3
# 	prices[i] = price / 100 * 90
# 	i += 1
#
# print(prices)
## FOR VARIANT1
# i = 0
# prices = [40, 42, 50, 60]
#
# for price in prices:
# 	prices[i] = price / 100 * 90
# 	i += 1
#
# print(prices)

## FOR VARIANT 2

#         0   1   2   3
prices = [40, 42, 50, 60]

# for i in range(len(prices)):  # len(prices) = 4
# 	prices[i] = prices[i] / 100 * 90
#
# print(prices)

############
## RANDOM LIST
from random import randint

numbers = []
begin = int(input("Begin of range: "))
end = int(input("End of range: "))
count = int(input("Length: "))

for i in range(count):
	numbers.append(randint(begin, end))

print(numbers)
