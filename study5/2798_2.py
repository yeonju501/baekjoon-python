import sys
sys.stdin = open('2798_input.txt')
def comb(n, r, hap):
    global ans
    if r == 0:
        if ans < hap <= M:
            ans = hap
        return
    elif n < r:
        return
    else:
        comb(n-1, r-1, hap+arr[n-1])
        comb(n-1, r, hap)


N, M = map(int, input().split())
ans = 0
A = [0] * N
arr = list(map(int, input().split()))

comb(N, 3, 0)
print(ans)
