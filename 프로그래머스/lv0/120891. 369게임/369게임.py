def solution(order):
    clap = [3, 6, 9]
    return len([i for i in str(order) if int(i) in clap])