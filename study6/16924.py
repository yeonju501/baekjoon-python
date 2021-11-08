import copy
import sys
sys.stdin = open('16924_input.txt')

def dfs(i, j):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for s in range(1, N):
        flag = 1
        for d in range(4):
            di = i + dx[d] * s
            dj = j + dy[d] * s
            if 0 <= di < N and 0 <= dj < M and arr[di][dj] == '*':
                pass
            else:
                flag = 0
                break
        if flag:
            rst.append([i + 1, j + 1, s])
            visited[i][j] = '.'
            for z in range(4):
                nx = i + dx[z] * s
                ny = j + dy[z] * s
                visited[nx][ny] = '.'
        else:
            break


N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = copy.deepcopy(arr)
rst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            dfs(i, j)

hap = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == '*':
            hap += 1

if hap == 0:
    print(len(rst))
    for i in rst:
        print(*i)
else:
    print(-1)
