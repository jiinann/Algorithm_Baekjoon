def solution(n):
    count = 0
    for i in range(1, n + 1):
        mixed = []
        for j in range(1, n + 1):
            if i % j == 0:
                mixed.append(j)
        if len(mixed) >= 3:
            count +=1
    return count