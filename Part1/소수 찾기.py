N = int(input())
test = map(int, input().split())
prime_num = 0

for i in test:
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j  == 0:
                error += 1
        if error == 0:
            prime_num += 1
print(prime_num)