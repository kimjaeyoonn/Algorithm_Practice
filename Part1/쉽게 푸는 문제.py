s, f = map(int, input().split())
temp = []

for i in range(1, f+1):
    for j in range(i):
        temp.append(i)
    if len(temp) >= f:
            break
print(sum(temp[s-1:f]))