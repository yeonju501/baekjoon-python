import sys
sys.stdin = open('2798_input.txt')

def perm(n, k, hap):
    global ans
    if hap > M:
        return
    if k == 3:
        if ans < hap <= M:
            ans = hap
        return
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                perm(n, k+1, hap+arr[i])
                used[i] = 0




N, M = map(int, input().split())
used = [0] * N
ans = 0
arr = list(map(int, input().split()))
perm(N, 0, 0)
print(ans)