import sys
sys.stdin = open('1149_input.txt')

def perm(n, k, hap):
    global ans
    if hap > ans:
        return
    if n == k:
        if hap < ans:
            ans = hap
    else:
        for i in range(3):
            if k == 0 or (k != 0 and used[k-1] != i):
                used[k] = i
                perm(n, k+1, hap+h[k][i])
                used[k] = 4

N = int(input())
h = [list(map(int, input().split())) for _ in range(N)]
used = [4] * N
ans = 1000001
perm(N, 0, 0)
print(ans)
