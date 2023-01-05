def solution(s1, s2):
    c = 0
    for s in s1:
        if s in s2:
            c += 1
    return c