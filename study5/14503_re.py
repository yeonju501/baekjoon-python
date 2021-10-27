def dfs(x, y, d) :
    global cnt

    for i in range(4) :
        nd = (d+3) % 4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if arr[nx][ny] == 0 and visit[nx][ny] == 0 :
            visit[nx][ny] = 1
            cnt += 1
            dfs(nx,ny,nd)

            visit[nx][ny] = 0
            return
        d = nd
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    dfs(nx,ny,d)




N,M = map(int,input().split())
r, c, d = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N) ]
visit = [[0] * M for _ in range(N)]
cnt = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visit[r][c] = 1
dfs(r,c,d)
print(cnt)