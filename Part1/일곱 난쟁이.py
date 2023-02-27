# 순열 사용
from itertools import combinations

P = [int(input()) for _ in range(9)]
C = list(combinations(P, 7))

for c in C:
    if sum(list(c)) == 100:
        answer=sorted(list(c))
        break

for i in answer:
    print(i)