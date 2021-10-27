import sys
sys.stdin = open('14503_input.txt')

def dfs(x, y, d):
    global cnt
    for i in range(4):
        nd = (d+3) % 4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if arr[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny, nd)
            visited[nx][ny] = 0
            return
        d = nd
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    dfs(nx, ny, d)



N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(M)]
dx = [-1, 0, 1, 0] # 좌 하 우 상
dy = [0, 1, 0, -1]
cnt = 1
visited[r][c] = 1
dfs(r, c, d)

print(cnt)

