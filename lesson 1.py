# 1st program
print(9**0.5 * 5)


# 2st program
print(9.99 > 9.98 and 1000 != 1000.1)


# 3rd program
def num(number):
    return number // 10 % 100
a = 1234
b = 5678
print(num(a) + num(b))


# 4th program
def left_num(number):
    return int(number)
def right_num(number):
    return int(number * 100 % 100)
c = 13.42
d = 42.13


print(left_num(c) == right_num(c) or left_num(d) == right_num(d))
