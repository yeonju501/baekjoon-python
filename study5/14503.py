import sys
sys.stdin = open('14503_input.txt')
def change(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def check(x, y, d):
    cnt = 1
    arr[x][y] = 2
    while True:
        dc = d
        for i in range(4):
            flag = 0
            dc = change(dc)
            di = x+dx[dc]
            dj = y+dy[dc]
            if 0 <= di < N and 0 <= dj < M and arr[di][dj] == 0:
                cnt += 1
                x = di
                y = dj
                arr[di][dj] = 2
                d = dc
                flag = 1
                break
        if flag == 0:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
            if arr[x][y] == 1:
                break
    return cnt


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]
print(check(r, c, d))