import sys
sys.stdin = open('15649_input.txt')


def perm(n, r, k):
    if k == r:
        for i in range(M):
            print(p[i], end=' ')
        print()
        return
    else:
        for i in range(N):
            if used[i] == 0:
                p[k] = arr[i]
                used[i] = 1
                perm(n, r, k + 1)
                used[i] = 0

N, M = map(int, input().split())
arr = list(range(1, N+1))
p = [0] * M
used = [0] * N
perm(N, M, 0)