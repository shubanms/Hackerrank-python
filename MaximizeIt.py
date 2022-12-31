from itertools import product

K, M = list(map(int, input().strip().split(" ")))
lst = []

for i in range(K):
    inp = list(map(int, input().strip().split(" ")))
    lst.append(inp[1:])

pro = list(product(*lst))

def power(x):
    total = 0
    for n in x:
        total += n ** 2
        
    return total % M

print(max(list(map(power, pro))))
