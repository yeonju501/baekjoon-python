import copy
import sys
sys.stdin = open('9663_input.txt')

def perm(n, k):
    global ans
    if n == k:
        arr = [[0] * N for _ in range(N)]
        for i in range(n):
            if arr[i][p[i]] == 1:
                return
            else:
                arr[i][p[i]] = 1
            for j in range(1, n):
                if 0 <= p[i] + j < n and 0 <= i + j < n:
                    arr[i+j][p[i]+j] = 1
                if 0 <= p[i] - j < n and 0 <= i + j < n:
                    arr[i + j][p[i] - j] = 1

        ans += 1
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                p[k] = i
                perm(n, k+1)
                used[i] = 0


N = int(input())
used = [0] * N
p = [0] * N
ans = 0
perm(N, 0)
print(ans)