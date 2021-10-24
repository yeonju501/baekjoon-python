import sys
sys.stdin = open('15662_input.txt')

def check_right(n, d):
    if d:
        if n+1 <= T and arr[n][idx[n][1]] != arr[n+1][idx[n+1][2]]:
            idx[n+1][3] = -d
            d = -d
        else:
            d = 0
    else:
        d = 0
    return d

def check_left(n, d):
    if d:
        if n-1 > 0 and arr[n][idx[n][2]] != arr[n-1][idx[n-1][1]]:
            idx[n-1][3] = -d
            d = -d
        else:
            d = 0
    else:
        d = 0
    return d

T = int(input())
arr = list()
arr.append([0, 0, 0, 0, 0, 0, 0, 0])
arr += [list(map(int, input())) for _ in range(T)]
idx = [[0, 2, 6, 0] for _ in range(T+1)]
K = int(input())
for i in range(K):
    N, D = map(int, input().split())
    idx[N][3] = D
    if T > 1:
        left = check_left(N, D)
        if N-1 > 1:
            for j in range(N-1, 1, -1):
                left = check_left(j, left)
        right = check_right(N, D)
        if N+1 < T:
            for j in range(N+1, T):
                right = check_right(j, right)
    for j in range(1, T+1):
        if idx[j][3]:
            idx[j][0] -= idx[j][3]
            idx[j][1] -= idx[j][3]
            idx[j][2] -= idx[j][3]
            idx[j][3] = 0

cnt = 0
for i in range(1, T+1):
    if arr[i][idx[i][0]]:
        cnt += 1

print(cnt)
