answer = []
def solution(num_list):
    for i in range(len(num_list)):
        i  = num_list[len(num_list) - 1 - i]
        answer.append(i)
    return answer