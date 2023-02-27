A = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(len(A)):
    A[i].sort(reverse=True)
    print(A[i][2])