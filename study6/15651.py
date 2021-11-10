import sys
sys.stdin = open('15651_input.txt')

def comb(n, r, k, s):
    if r == k:
        print(*c)
    else:
        for i in range(s, n):
            c[k] = arr[i]
            comb(n, r, k+1, i)

N, M = map(int, input().split())
arr = range(1, N+1)
c = [0] * M
comb(N, M, 0, 0)