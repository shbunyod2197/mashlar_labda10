# 1
res = lambda a, b: a if a == b else(1 if a > b else -1)
print(res(3,5))

# 2
res = lambda a: 'Fizz' if a % 3 == 0 else a
print(res(8))

# 3
res = lambda a: "OK" if a % 2 == 0 and a % 3 == 0 else "NO"
print(res(6))

# 4
res = lambda a:"ReZero" if a == 0 else "NOT Zero"
print(res(0))

# 5
res = lambda a: "Range" if 1 <= a <= 10 else "Out"
print(res(7))

# 6
res = lambda a, b: a + b > 50
print(res(8, 9))

# 7
res = lambda a:"Good" if  a % 2 == 0 and a > 0 else "Bad"
print(res(80))

# 8
res = lambda a: a ** 2 if a % 4 == 0  else a * 3
print(res(8))

# 9-m
f = lambda x: x if x >= 10 else 10
print(f(6))

# 10-m
f = lambda a, b: a if a == b else (a + b) / 2
print(f(5, 5))
