def solution(numbers):
    numbers_sort = sorted(numbers, reverse = True)
    return numbers_sort[0] * numbers_sort[1]