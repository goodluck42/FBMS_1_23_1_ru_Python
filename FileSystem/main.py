# r - read
# w - write
# r+, w+ - read & write
# a - append
# a+ - append & read



## list generators / list comprehesion
# from random import randint
#
# values = [randint(0, 100) for i in range(10)]
# evens = [i for i in values if i % 2 == 0]
#
# print(values)
# print(evens)

## file write
# fd = open("data.txt", 'w')  # truncate
#
# fd.write("Hello C++!\n")
#
# # names = [item + '\n' for item in ["John", "Rick", "Alex"]]
# names = ["John", "Rick", "Alex"]
#
# ## variant1
# # for i in range(len(names)):
# #     fd.write(names[i])
# #     fd.write('\n')
# ## variant2
#
# for i in range(len(names)):
#     names[i] = names[i] + '\n'
#
# fd.writelines(names)
#
# fd.close()


## file append

# fd = open("data.txt", 'a')
#
# fd.write("Josh\n")
#
# fd.close()

## file read
# fd = open("data.txt", 'r')
# word1 = fd.read(5)
# fd.read(1)
# lang = fd.read(5)
#
# print(word1)
# print(lang)
#
# fd.seek(0)  # передвигает каретку в начало
# lines = fd.readlines()   # возвращает список
#
# print(lines)
#
# fd.seek(0)
# line = fd.readline(5)
#
# print(line)
#
# fd.close()


#############

import json

## write json
# students = []
#
# students.append({
#     "coins": 90,
#     "crystals": 115,
#     "name": "Vadim"
# })
#
# students.append({
#     "coins": 45,
#     "crystals": 99,
#     "name": "Seymur"
# })
#
#
# with open("students.json", 'w') as fd:
#     json.dump(students, fd)

## read json


# with open("students.json", 'r') as fd:
#     students = json.load(fd)
#
# print(students)
