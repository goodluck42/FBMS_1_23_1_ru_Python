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

while i < 20:
    if i >= 10 and i <= 15:
        i += 1
        continue

    print(i)
    i += 1

# [0, 100]
value = 900

if value >= 0 and value <= 100:
    print("in range")
else:
    print("not in range")




