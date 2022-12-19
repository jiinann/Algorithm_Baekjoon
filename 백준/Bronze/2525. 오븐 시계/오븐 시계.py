A, B = map(int, input().split())
C = int(input())
done = (A * 60) + B + C
if done >= 1440:
    print(done // 60 - 24, done % 60)
else:
    print(done // 60, done % 60)