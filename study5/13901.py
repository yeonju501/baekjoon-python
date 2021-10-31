import sys
sys.stdin = open('13901_input.txt')

def change(s):
    if s == 1:
        return 0
    elif s == 2:
        return 1
    elif s == 3:
        return 2
    elif s == 4:
        return 3

def dfs(x, y, d):
    d = d
    while True:
        flag = 0
        for i in range(4):
            dd = change(direction[d])
            di = x + dx[dd]
            dj = y + dy[dd]
            if 0 <= di < R and 0 <= dj < C and arr[di][dj] == 0:
                arr[di][dj] = 1
                x = di
                y = dj
                break
            else:
                flag += 1
                d = (d+1)%4
                if flag == 4:
                    return x, y


R, C = map(int, input().split())
k = int(input())
arr = [[0] * C for _ in range(R)]
dx = [-1, 1, 0, 0] #
dy = [0, 0, -1, 1]
for i in range(k):
    x, y = map(int, input().split())
    arr[x][y] = 2
sr, sc = map(int, input().split())
direction = list(map(int, input().split()))
arr[sr][sc] = 1
x, y = dfs(sr, sc, 0)
print(x, y)
