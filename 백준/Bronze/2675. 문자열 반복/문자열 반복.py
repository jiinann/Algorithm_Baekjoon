T = int(input())
for i in range(T):
    R, S = input().split()
    print("".join([j * int(R) for j in S]))