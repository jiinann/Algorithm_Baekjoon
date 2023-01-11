def solution(cipher, code):
    ans_list = []
    for i in range(len(cipher)):
        if int(i + 1) % code == 0:
            ans_list.append(cipher[i])
    return ''.join(ans_list)