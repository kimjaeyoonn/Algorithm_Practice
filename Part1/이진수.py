T = int(input())
temp = []

for i in range(1, T+1):
    N = int(input())
    temp.append(N)

for i in temp:
    l = -1
    test = bin(i)
    for j in range(len(test), 2, -1):
        l+=1
        if test[j-1] == '1':
            print(l, end=' ')
    print('')