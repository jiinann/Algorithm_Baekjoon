def solution(my_string):
    num = 0
    for i in my_string:
        try:
            if type(int(i)) == int:
                num += int(i)
        except:
            pass
    return num