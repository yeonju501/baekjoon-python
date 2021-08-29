import sys
sys.stdin = open('2615_input.txt')

def check():
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    cnt = 1
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    while 0 <= nx < N and 0 <= ny < N and arr[i][j] == arr[nx][ny]:
                        cnt += 1
                        if cnt == 5:
                            if 0 <= nx + dx[d] < N and 0 <= ny + dy[d] < N and arr[nx][ny] == arr[nx + dx[d]][ny + dy[d]]:
                                break
                            if 0 <= i - dx[d] < N and 0 <= j - dy[d] < N and arr[i][j] == arr[i - dx[d]][j - dy[d]]:
                                break
                            return arr[i][j], i, j
                        nx += dx[d]
                        ny += dy[d]
    return 0, 0, 0

N = 19
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 1, 0, -1] # 우 우하 하 우상
dy = [0, 1, 1, 1]
winner, x, y = check()
if winner:
    print(winner)
    print(x+1, y+1)
else:
    print(winner)




