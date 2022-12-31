def solution(num_list):
    even = []
    odd = []
    answer = []
    for i in num_list:
        even.append(i) if i % 2 == 0 else odd.append(i)
    answer.append(len(even))
    answer.append(len(odd))
    return answer