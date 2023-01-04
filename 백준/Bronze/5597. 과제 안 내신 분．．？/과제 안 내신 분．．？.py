sub = [int(input()) for i in range(28)]
stud = list(range(1, 31, 1))
sub_x = [x for x in stud if x not in sub]
print(min(sub_x))
print(max(sub_x))