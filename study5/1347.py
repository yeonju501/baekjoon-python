import sys
sys.stdin = open('1347_input.txt')

dx = [1, 0, -1, 0] # 하 좌 상 우
dy = [0, -1, 0, 1]
arr = [['#'] * 100 for _ in range(100)]
N = int(input())
txt = input()
d = 0
i = j = 50
arr[i][j] = '.'
for s in range(N):
    if txt[s] == 'R':
        if d != 3:
            d += 1
        else:
            d = 0
    elif txt[s] == 'L':
        if d != 0:
            d -= 1
        else:
            d = 3
    else:
        i += dx[d]
        j += dy[d]
        arr[i][j] = '.'
xs = []
ys = []
for i in range(100):
    for j in range(100):
        if arr[i][j] == '.':
            xs.append(i)
            ys.append(j)
for i in range(min(xs), max(xs)+1):
    for j in range(min(ys), max(ys)+1):
        print(arr[i][j], end='')
    print()




