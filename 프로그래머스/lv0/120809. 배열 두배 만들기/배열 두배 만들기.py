def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        i = numbers[i] * 2
        answer.append(i)
    return answer