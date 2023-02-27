n,k = map(int, input().split())
m = 0

# n의 약수
for i in range(1, n+1):
    if n%i == 0:
        m += 1
        if m == k:
            print(i)
        
if m < k:
    print(0)