
import sys
sys.stdin = open('1012_input.txt')


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for i in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    t = 0
    q = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                q.append([i, j])
                field[i][j] = -1
                while True:
                    y, x = q.pop(0)
                    for d in range(4):
                        nX = dx[d] + x
                        nY = dy[d] + y
                        if 0 <= nX < M and 0 <= nY < N:
                            if field[nY][nX] == 1:
                                field[nY][nX] = -1
                                q.append([nY, nX])
                    if not q:
                        t += 1
                        break
    print(t)


