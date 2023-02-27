# 배열 입력 방법 기억할것.
p = 0
max = p
train = [list(map(int, input().split())) for _ in range(10)]
for i in range(len(train)):
    p -= train[i][0]
    p += train[i][1]
    if p > max:
        max = p
print(max)