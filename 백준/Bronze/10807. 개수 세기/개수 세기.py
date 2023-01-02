N = int(input())
nums = map(int, input().split())
v = int(input())
total = 0
for num in nums:
    if num == v:
        total += 1
    else:
        pass
print(total)