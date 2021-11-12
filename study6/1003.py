import sys
sys.stdin = open('1003_input.txt')

def fibo(n):
    if n >= 2 and len(memo) <= n:
        memo.append([memo[n-1][0]+memo[n-2][0], memo[n-1][1]+memo[n-2][1]])
    return memo[n]


tc = int(input())
memo = [[1, 0], [0, 1]]
ns = [int(input()) for _ in range(tc)]
for i in range(max(ns)+1):
    fibo(i)

for i in range(len(ns)):
    print(*fibo(ns[i]))


