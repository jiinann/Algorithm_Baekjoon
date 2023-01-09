def solution(n, t):
    return [n* (2 **t) for t in range(t + 1)][-1]