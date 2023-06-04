# print(1, 2, 3, sep="", end="")
# print(4, 5, 6)

###########################
## WHILE & BREAK
# i = 0
# max_i = int(input())
#
# while i < max_i:  # max_i = 2000
#     if i >= 1000:
#         print("limit exceeded")
#         break
#
#     if i % 2 == 0:
#         print(i)
#
#
#     # print("iteration #", i, sep="")
#     i += 1
#
#     # # i -= 1  # decrement
#     # i += 1  # increment
#
# # iteration - одно выполнение блока кода цикла
# # decrement - уменьшение переменной на 1
# # increment - увеличение переменной на 1
# print("i = ", i)

i = 0

# [10, 15]

# while i < 20:
#     if i >= 10 and i <= 15:
#         i += 1
#         continue
#
#     print(i)
#     i += 1
#
# # [0, 100]
# value = 900
#
# if value >= 0 and value <= 100:
#     print("in range")
# else:
#     print("not in range")


# a = 42
# b = 13
#
# (a, b) = (b, a)

# temp = a
# a = b
# b = temp

# print("a = ", a)
# print("b = ", b)
#
#
#
# begin = int(input())
# end = int(input())
#
# begin_copy = begin
#
# print("first loop: ")
# while begin < end:
#     print(begin)
#     begin += 1
#
#
# begin = begin_copy
#
# print("second loop: ")
# while begin < end:
#     print(begin)
#     begin += 1
#


i = 100
c = 0
while i < 9999:
    lim = 0
    if i < 1000:
        lim = 3
    else:
        lim = 4

    v = set(list(str(i)))

    if len(v) == lim:
        c += 1

    i += 1

print(c)