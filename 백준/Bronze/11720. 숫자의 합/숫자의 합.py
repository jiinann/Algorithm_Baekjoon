N = input()
num = input()
print(sum([int(i) for i in num]))
assert len(num) != N, 'num is invalid'