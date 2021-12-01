import sys
sys.stdin = open('9908_input.txt')

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    space = [[0] * M for _ in range(N)]
    for i in range(K):
        r, c = map(int, input().split())
        space[r][c] = 1
    q = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    t = 1
    m = 0
    for i in range(N):
        for j in range(M):
            if space[i][j] == 1:
                if m < t:
                    m = t
                t = 1
                q.append([i, j])
                space[i][j] = -1
                while True:
                    x, y = q.pop(0)
                    for d in range(4):
                        nX = dx[d] + x
                        nY = dy[d] + y
                        if 0 <= nX < N and 0 <= nY < M:
                            if space[nX][nY] == 1:
                                space[nX][nY] = -1
                                t += 1
                                q.append([nX, nY])
                    if not q:
                        break
    print(m)



"""
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
"""