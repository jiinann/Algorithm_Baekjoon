def solution(array, height):
    total = 0
    for i in array:
        if i > height:
            total += 1
        else:
            pass
    return total