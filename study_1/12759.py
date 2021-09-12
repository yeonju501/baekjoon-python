# 이차원배열을 채워준다 0으로 그리고 1 2로 채우자
# 대각선 (1,1 2,2 3,3), (1,3 2,2, 3,1)
# 행방향 (1,1 1,2 1,3) (2,1 2,2 2,3) (3,1 3,2 3,3)
# 열방향 (1,1 2,1 3,1) (1,2 2,2 3,2) (1,3 2,3 3,3)
# 나오는 같은 숫자가 3번 나오면 이긴다 x나 y가
# 대각선은?
# 검사를 해야한다. 6번을 받아서 확인 나머지 세개를 입력 받아서 확인?

import sys
sys.stdin = open('12759_input.txt')
input = sys.stdin.readline
arr = [[0] * 3 for _ in range(3)]
x1 = [[0,0], [1,1], [2,2]]
x2 = [[0,2], [1,1], [2,0]]
p = int(input())
for i in range(9):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if i % 2 == 0 and p == 1 or i % 2 and p == 2:
        arr[x][y] = 1
        for j in range(3):
            if arr[x][j] != 1:
                break
        else:
            print(1)
            break
        for j in range(3):
            if arr[j][y] != 1:
                break
        else:
            print(1)
            break
        if [x, y] in x1:
            if arr[0][0] == 1 and arr[1][1] == 1 and arr[2][2] == 1:
                print(1)
                break
        if [x, y] in x2:
            if arr[2][0] == 1 and arr[1][1] == 1 and arr[0][2] == 1:
                print(1)
                break
    elif i % 2 and p == 1 or i % 2 == 0 and p == 2:
        arr[x][y] = 2
        for j in range(3):
            if arr[x][j] != 2:
                break
        else:
            print(2)
            break
        for j in range(3):
            if arr[j][y] != 2:
                break
        else:
            print(2)
            break
        if [x, y] in x1:
            if arr[0][0] == 2 and arr[1][1] == 2 and arr[2][2] == 2:
                print(2)
                break
        if [x, y] in x2:
            if arr[0][2] == 2 and arr[1][1] == 2 and arr[2][0] == 2:
                print(2)
                break
else:
    print(0)
