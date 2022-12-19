H, M = map(int, input().split())
alarm = (H * 60) + M - 45
if H == 0 and 45<= M <= 59:
    print(alarm // 60, alarm % 60)
elif H == 0 and 0 <= M <= 44:
    print(alarm // 60 + 24, alarm % 60)
else:
    print(alarm // 60, alarm % 60)