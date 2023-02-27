def prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

temp = []

M = int(input())
N = int(input())

for i in range(M, N+1):
    if prime(i) == True:
        temp.append(i)
if len(temp) == 0:
    print(-1)
else:
    print(sum(temp))    
    print(min(temp))