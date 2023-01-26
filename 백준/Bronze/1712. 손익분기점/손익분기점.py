A, B, C = map(int, input().split())
try:
    print(int(A / (C - B) + 1) if A / (C - B) > -1 else -1)
except:
    print(-1)