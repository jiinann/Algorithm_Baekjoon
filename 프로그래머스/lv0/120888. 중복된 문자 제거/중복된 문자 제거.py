def solution(my_string):
    final = ''
    for i in my_string:
        if i in final:
            pass
        else:
            final += i
    return final