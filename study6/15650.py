import sys
sys.stdin = open('15650_input.txt')

def comb(n, r, k, s): # k는 고른 개수 s는 시작 지점
    if k == r:
        print(*a)
    else:
        for i in range(s, n-r+k+1): # n-r+k는 고를 수 있는 지점의 범위
            a[k] = arr[i]
            comb(n, r, k+1, i+1)


N, M = map(int, input().split())
arr = range(1, N+1)
a = [0] * M
comb(N, M, 0, 0)

