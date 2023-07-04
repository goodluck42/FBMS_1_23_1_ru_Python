#    0123456789
s = "Python is the best language for AI"
# print(s)
## slices
# word = s[:6]
# word2 = s[19:27]
# word3 = s[-2:]
#
# print(word)
# print(word2)
# print(word3)

## replace
# s = s.replace("Python", "C++")
# s = s.replace("AI", "gamedev")
#
# print(s)

## count

# cnt = s.count('a')
#
# print(cnt)

## split & join
##  ["Python", "is", "the", "best", "language", "for", "AI"]
# words = s.split(' ')  # words это список из слов
#
# words_len = len(words)
#
# print(words)
# print(f"words length = {words_len}")
#
# words[-1] = "backend"
#
# text = '|'.join(words)
#
# # a = '@'  # char
# # b = "C++"  # str
#
# print(text)

## index

# target = input("Enter word: ")
#
# if target in s:
#     idx = s.index(target)
#     print(f"index = {idx}")
# else:
#     print(f"word '{target}' not found")

## find

# idx = s.find("worst")
#
# print(idx)

## is methods
## isalpha
# text = "C++"
#
# if text.isalpha():
#     print(f"{text} is alpha")
# else:
#     print(f"{text} is not alpha")


## isalnum

# text = "C99"
#
# if text.isalnum():
#     print(f"{text} is alpha or numeric")
# else:
#     print(f"{text} is not alpha or numeric")

## ascii

# text = 'abcş'
#
# if text.isascii():
#     print(f"'{text}' is ascii")
# else:
#     print(f"'{text}' is not ascii")


## isnumeric

text = "42"

if text.isnumeric():
    print("OK")

## startswith & endswith

# text = "C++ is the best lang for gamedev"
#
# if text.startswith("C++"):
#     print("starts")
# else:
#     print("not starts")


# if text.endswith("dev"):
#     print("ends")
# else:
#     print("not ends")

## lower & upper

# text = "Python!"
#
# # text = text.lower()
# text = text.upper()
#
# print(text)

## Escape sequences

print("C++\n\n\nC#")
print("C++\t\tC#")
print("C++\b\b#")
print("Python is the \"best\" language")
print("\\n\\n")

print("-" * 12)
x = 5
print("C++\nC#", end='')
print('\n', end='')
print(x, end='')