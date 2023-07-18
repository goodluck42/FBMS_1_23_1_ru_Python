# fd = open("expr.txt", 'r')
#
# lines = [line.replace('\n', '') for line in fd.readlines()]
#
# print(lines)
#
# fd.close()
#
# vowels = "aiuo"
# consonants = "bcmn"
#
#
# def count_vowels_and_consonants(filename):
#     vowel_count = 0
#     consonant_count = 0
#
#     fd = open(filename, 'r')
#
#     # 2TODO: write an algorithm
#
#     fd.close()
#
#     return 42, 13

#######################################
#####
# import my_math
#
# r = my_math.div(10, 0)
#
# print(r)
#####
# from my_math import div, mult, add
#
# r = add(div(10, 2), mult(2, 5))
#
# print(r)
#####

# from my_math import div, add, mult
#
#
# def div(a, b):
#     return a / b
#
#
# r = add(div(10, 0), mult(2, 5))
#
# print(r)
#####

# from my_math import div as my_div, add, mult
#
# def div(a, b):
#     return a / b
#
#
# r = add(my_div(10, 0), mult(2, 5))
#
# print(r)
#####
# import random as rnd
#
# random = rnd.randint(13, 42)
#
# print(random)


# def f(a=5, b=10):
#     return a + b


# f(10)  # f(10, 10)
# f(b=15, a=10)  # f(10, 15)
# f(b=5)  # f(5, 5)
# f()  # f(5, 10)
#
#
# def main():
#     users = []
#
#     print(users)
#
#
# if __name__ == '__main__':
#     main()
#
#
# def a():
#     print("a")
#
#     return False
#
#
# def b():
#     print("b")
#
#     return True
#
#
# if a() and b():
#     print("OK")
# else:
#     print("fail")
#
#
# def f(f):
#     return f * 2
#
#
# res = f(f(5))
#
# print(res)


# s = 3
#
# match s:
#     case 2:
#         print("s is 2")
#     case 3:
#         print("s is 3")
#
#
# def say_hi():
#     print("hi")
#
#
# r = say_hi()
#
# print(r)

s = 0
def my_print():
    s = 90

    print(s)