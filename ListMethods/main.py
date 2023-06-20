# my_list = [10, 20, 30, 40]
#  len(my_list) = 4
# for i in range( 4 ):
# for i in range(len(my_list)):
#     if i % 2 == 0:
#         my_list[i] -= 5
#     # print(i, my_list[i])
#
# print(my_list)

# i = 0
#
# while i < len(my_list):
#     if i % 2 == 0:
#          my_list[i] -= 5
#
#     i += 1
#
# print(my_list)

# int, float, str, bool, char - immutable (неизменяемые)
# list - mutable (изменяемые)
##########
# list, str - reference type (ссылочные типы)
# int, float, bool, char - value type (значимые типы)
#
###############
# a = []
# b = a
#
# a.append(10)
# a.append(15)
#
# print(a)
# print(b)

#################
## immutability
# a = 10
# print(hex(id(a)))  # выводим адрес на экран
# a = 90
# print(hex(id(a)))  # выводим адрес на экран
# a = 10
# print(hex(id(a)))  # выводим адрес на экран

#################
# mutability
#    v0  v1
# l = [20, 20]
#
# l.append(90)
#
# print(hex(id(l[0])))
# print(hex(id(l[1])))

### str immutability

# s = "Python"
#
# print(hex(id(s)))
#
# s += "!"
#
# print(hex(id(s)))
#
# print(s)


## insert

# my_list = [10, 42, 30, 13]
#
# my_list.insert(1, 90)
#
# print(my_list)

## pop

# my_list = [10, 42, 15, 90, 30, 13]
#
# my_list.pop(1)  # [10, 15, 90, 30, 13]
# my_list.pop(2)  # [10, 15, 30, 13]
#
# print(my_list)


## clear

# my_list = [10, 42, 15, 90, 30, 13]
#
# my_list.clear()
#
# print(my_list)

## remove

# langs = ["C", "C++", "C++", "C#", "Python"]

# try:
#     i = langs.index("Python")
#     print("index =", i)
# except:
#     print("an error occurred")

# if "Python" in langs:
#     langs.remove("Python")
# else:
#     print("Python does not exist")
#
# print(langs)

## extend + operator +

# my_list = [10, 20, 30]
# target = [1, 13, 42]
#
# my_list.extend(target)
#
# print(my_list)
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# c = a + b
# print("a =", a)
# print("b =", b)
# print("c =", c)

## sort

# my_list = [10, 42, 15, 90, 30, 13]
#
# # my_list.sort()  # ascending
# my_list.sort(reverse=True)  # descending
#
# print(my_list)

## copy

# my_list = [10, 42, 15, 90, 30, 13]
# my_copy = my_list.copy()
#
# print(my_list)
# print(my_copy)

my_list = [10, 42, 15, 15, 30, 13]

cnt = my_list.count(15)

print(cnt)