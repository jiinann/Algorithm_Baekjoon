nums = [int(input()) for i in range(10)]
rest = [num % 42 for num in nums]
print(len(set(rest)))