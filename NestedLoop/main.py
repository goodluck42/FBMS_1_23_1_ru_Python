# i = 0
#
# while i < 5:
# 	print(i)
# 	i += 1
################
## range(end)
# for i in range(5):  # 0 1 2 3 4
# 	print(i)

################
## range(begin, end, step)
# for i in range(3, 10, 2):  # 3 4 5 ... 9
# 	print(i)
################
# i = 0
#
# while i < 5:
# 	if i == 3:
# 		continue
#
# 	print(i)
#
# 	i += 1
################
# for i in range(5):
# 	if i == 3:
# 		continue
# 	print(i)
################

# my_range = range(3, 10, 2)
#
# print(list(my_range))
#
# for i in my_range:
# 	i += 100
# 	print(i)


# int, float, bool, str
#

# a = 42  #
# b = a
# a = 10
#
# print(b)

# 1 2 3 4 5


# a = 10
# b = 20
#
# temp = a
# a = b
# b = temp
#
# print(a + b)
#
#
# r = -(2 - 1 / 2 - 2)


x = 0

while x < 10:
	if x == 3 or x == 4 or x == 5:
		print("skip")
	x += 1