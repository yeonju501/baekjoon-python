import sys
sys.stdin = open('14889_input.txt')

def comb(n, r, k, s):
    global ans
    if r == k:
        t1 = []
        t2 = []
        val = 0
        for i in range(1, N+1):
            if i in t:
                t1.append(i)
            else:
                t2.append(i)
        for i in t1:
            for j in t1:
                if i == j:
                    continue
                val += adj[i-1][j-1]
        for i in t2:
            for j in t2:
                if i == j:
                    continue
                val -= adj[i - 1][j - 1]
        if abs(val) < ans:
            ans = abs(val)
    else:
        for i in range(s, n-r+k+1):
            t[k] = arr[i]
            comb(n, r, k+1, i+1)





# 4개 중에 두 개를 뽑아라 아니면 아닌 애들로
N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
arr = range(1, N+1)
t = [0] * (N//2)
ans = 987654321
comb(N, N//2, 0, 0)
print(ans)