import sys
sys.stdin = open('5212_input.txt')

import copy

def check(i, j):
    c = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for d in range(4):
        di = i + dx[d]
        dj = j + dy[d]
        if di < 0 or di >= R or dj < 0 or dj >= C:
            continue
        if arr[di][dj] == 'X':
            continue
        c += 1
    return c



R, C = map(int, input().split())
C += 2
arr = [['.'] * C]
for i in range(R):
    a = ['.']
    a += input()
    a += ['.']
    arr.append(a)
R += 2
arr.append(['.'] * C)
arr2 = copy.deepcopy(arr)
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            cnt = check(i, j)
            if cnt >= 3:
                arr2[i][j] = '.'

x = []
y = []
for i in range(R):
    for j in range(C):
        if arr2[i][j] == 'X':
            x.append(i)
            y.append(j)

min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)
for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        print(arr2[i][j], end='')
    print()