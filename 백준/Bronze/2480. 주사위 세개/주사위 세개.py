A, B, C = map(int, input().split())
import statistics as stat
if A == B and B == C:
    print(10000 + A * 1000)
elif A != B and A != C and B != C:
    print(max(A, B, C) * 100)
else:
    print(1000 + stat.mode([A, B, C]) * 100)