def squarefun(a: int):
    l = []
    while (a!=0):
        l.append(a%10)
        a = a//10
    return sum([x*x for x in l])
m = 19
for i in range(10):
    if (m == 1):
        print(True)
        break 
    else:
        m = squarefun(m)
print(False)