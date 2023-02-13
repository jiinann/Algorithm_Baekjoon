def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    final = ''
    for i in my_string:
        if i not in vowels:
            final += i
    return final