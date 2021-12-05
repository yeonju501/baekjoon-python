import sys
sys.stdin = open('9290_input.txt')

def check(x, y):
    for d in range(8):
        di = x + dx[d]
        dj = y + dy[d]
        if 0 <= di < 3 and 0 <= dj < 3 and arr[di][dj] == k:
            if 0 <= di+dx[d] < 3 and 0 <= dj+dy[d] < 3 and arr[di+dx[d]][dj+dy[d]] == '-':
                arr[di+dx[d]][dj+dy[d]] = k
                return
        elif 0 <= di < 3 and 0 <= dj < 3 and arr[di][dj] == '-':
            if 0 <= di+dx[d] < 3 and 0 <= dj+dy[d] < 3 and arr[di+dx[d]][dj+dy[d]] == k:
                arr[di][dj] = k
                return


dx = [1, 1, 0, 1, -1, -1, -1, 0] # 하, 우하, 우, 좌하, 우상, 좌상, 상, 좌
dy = [0, 1, 1, -1, 1, -1, 0, -1]
for tc in range(1, int(input())+1):
    arr = [list(input()) for _ in range(3)]
    k = input()
    for i in range(3):
        for j in range(3):
            if arr[i][j] == k:
                check(i, j)
    print(f'Case {tc}:')
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end='')
        print()