def solution(my_string):
    answer = []
    for i in my_string:
        answer.append(i.upper() if i.islower() == True else i.lower())
    return "".join(answer)