# 3 6 9 ... 30

# a = 0
#
# while a <= 30:
#     if a == 0:
#         a += 3
#         continue
#     print(a)
#     a += 3

# i = 0
#
# while i < 5:
#     if i == 3:
#         print("found")
#         break
#     print(i)
#
#     i += 1
# else:
#     print("element not found")

##################################
# while True:
#     print("1. FirstTask")
#     print("2. SecondTask")
#     print("3. ThirdTask")
#     print("4. Exit")
#
#     task_n = int(input("Enter task number -> "))
#
#     if task_n == 1:
#         print("First task")
#         i = 0
#         while i < 10:
#             print(i)
#             i += 1
#     elif task_n == 2:
#         print("Second task")
#     elif task_n == 3:
#         print("Third task")
#     elif task_n == 4:
#         print("Goodbye")
#         break
################################
# import random
# from random import randint
#
# while True:
#     new_var = randint(10, 99)  # 1/90
#
#     print(new_var)
#
#     flag = int(input("Continue? 0 - no, 1 - yes; -> "))
#
#     if flag == 0:
#         break
######################
new_var = int(input())

# 1 -> 5

if new_var >= 1 and new_var <= 5:
    print("in range")
else:
    print("not in range")
