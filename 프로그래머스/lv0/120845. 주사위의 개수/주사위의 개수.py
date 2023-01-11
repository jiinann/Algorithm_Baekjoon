def solution(box, n):
    answer = 1
    for i in [(i // n) for i in box]:
        answer *= i
    return answer