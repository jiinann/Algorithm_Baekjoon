numbers = map(int, input().split())
positive = []
for i in numbers:
    if i > 0:
        positive.append(i)
print(len(positive))