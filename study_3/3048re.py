# 대각선의 개수  (N-3) * N / 2
n = int(input())
fac = 1
for i in range(n, n-4, -1):
    fac *= i
print(fac//24)