T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    i += 1
    print('Case #{}: {} + {} = {}'.format(i, A, B, A + B))