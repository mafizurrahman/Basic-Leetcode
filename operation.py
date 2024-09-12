new = []
operations = ['5', '2', 'C', 'D', '+']
for op in operations:
    if op == '+':
        new.append(new[-1] + new[-2])
    elif op == 'D':
        new.append(2 * new[-1])
    elif op == 'C':
        new.pop()
    else:
        new.append(int(op))

print(sum(new))