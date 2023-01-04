N = int(input())
g = list(map(int, input().split()))
best = max(g)
g_mod = [round(i / best * 100, 2) for i in g]
print(sum(g_mod) / N)