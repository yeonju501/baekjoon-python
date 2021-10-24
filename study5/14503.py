import sys
sys.stdin = open('14503_input.txt')

def check(r, c, d):
    dx = [0, 1, 0, -1] # 좌 하 우 상
    dy = [-1, 0, 1, 0]
    while True:
        flag = 0
        for i in range(4):
            arr[r][c] = 2
            dr = r + dx[d]
            dc = c + dy[d]
            if dr < 0 or dr >= N or dc < 0 or dc >= M or arr[dr][dc]:
                if d != 3:
                    d += 1
                else:
                    d = 0
                flag += 1
                continue
            r = dr
            c = dc
            break
        if flag == 4:
            dr = r - dx[d]
            dc = c - dy[d]
            if dr < 0 or dr >= N or dc < 0 or dc >= M or arr[dr][dc] == 1:
                return
            r = dr
            c = dc


N, M = map(int, input().split())
R, C, d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
if d == 0:
    d = 3
check(R, C, d)
cnt = 0

for i in range(N):
    print(arr[i])
    cnt += arr[i].count(2)
print(cnt)

