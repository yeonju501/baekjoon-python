import sys
sys.stdin = open('2072_input.txt')

T = int(input())
arr = [[0] * 19 for _ in range(19)]
b = 0
for i in range(T):
    b += 1
    x, y = map(int, input().split())
    arr[x-1][y-1] = b

dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]
w = []
m = 0
for i in range(19):
    for j in range(19):
        if arr[i][j] % 2:
            for d in range(4):
                m = arr[i][j]
                nx = i + dx[d]
                ny = j + dy[d]
                cnt = 1
                if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                    continue
                while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] % 2:
                    cnt += 1
                    if m < arr[nx][ny]:
                        m = arr[nx][ny]
                    if cnt == 5:
                        if 0 <= nx + dx[d] < 19 and 0 <= ny + dy[d] < 19 and arr[nx + dx[d]][ny + dy[d]] % 2:
                            break
                        if 0 <= i - dx[d] < 19 and 0 <= j - dy[d] < 19 and arr[i - dx[d]][j - dy[d]] % 2:
                            break
                        w.append(m)
                        break
                    nx += dx[d]
                    ny += dy[d]
for i in range(19):
    for j in range(19):
        if arr[i][j] % 2 == 0 and arr[i][j] != 0:
            for d in range(4):
                m = arr[i][j]
                nx = i + dx[d]
                ny = j + dy[d]
                cnt = 1
                if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                    continue
                while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] % 2 == 0 and arr[nx][ny] != 0:
                    cnt += 1
                    if m < arr[nx][ny]:
                        m = arr[nx][ny]
                    if cnt == 5:
                        if 0 <= nx + dx[d] < 19 and 0 <= ny + dy[d] < 19 and arr[nx + dx[d]][ny + dy[d]] % 2 == 0 and arr[nx + dx[d]][ny + dy[d]] != 0:
                            break
                        if 0 <= i - dx[d] < 19 and 0 <= j - dy[d] < 19 and arr[i - dx[d]][j - dy[d]] % 2 == 0 and arr[i - dx[d]][j - dy[d]] != 0:
                            break
                        w.append(m)
                        break
                    nx += dx[d]
                    ny += dy[d]

if w:
    print(min(w))
else:
    print(-1)