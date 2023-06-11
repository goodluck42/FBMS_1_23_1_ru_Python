# n = int(input())
#### WHILE VARIANT
# i = 0

# while i < 10:
# 	# print(n, "x", i + 1, "=", (i + 1) * n)
# 	b = i + 1
# 	print(f"{n} * {b} = {b * n}")
# 	i += 1
#### FOR VARIANT
# for i in range(1, 10 + 1):
# 	print(f"{n} * {i} = {i * n}")

#####################################

# begin = int(input("Enter begin -> "))
# end = int(input("Enter end -> "))

### FOR VARIANT
# for i in range(begin, end + 1):
# 	for j in range(1, 10 + 1):
# 		print(f"{i} * {j} = {i * j}")


### WHILE VARIANT

# i = begin
#
# while i <= end:
# 	j = 1
#
# 	while j <= 10:
# 		print(f"{i} * {j} = {i * j}")
# 		j += 1
#
# 	print("-" * 10)
#
# 	i += 1
#####################
# i = 0
#
# while i < 3:
# 	j = 0
# 	print("nested loop begin")
# 	while j < 3:
# 		print(f"i = {i}; j = {j}")
# 		j += 1
# 	print("nested loop end")
# 	i += 1

# i = 2 && j = 5

# for i in range(1, 4):
# 	break_required = False
#
# 	for j in range(1, 6):
# 		if i == 2 and j == 5:
# 			break_required = True
# 			break
# 		print(f"i = {i}; j = {j}")
# 	if break_required:
# 		break


for i in range(5):
	for j in range(5):
		if i >= 1 and i <= 3 and j >= 1 and j <= 3:
			print("  ", end="")
		else:
			print("* ", end="")
	print()