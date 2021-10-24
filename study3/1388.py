# 나무판자 정사각형
# 방 직사각형
# 같은 행에 인접해있다면 같은 나무 판자
import sys
sys.stdin = open('1388_input.txt')
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    flag = 0
    for j in range(M):
        if arr[i][j] == '-':
            if flag == 0:
                flag = 1
        if arr[i][j] == '|' and flag == 1:
            flag = 0
            cnt += 1
    if flag:
        flag = 0
        cnt += 1

for i in range(M):
    flag = 0
    for j in range(N):
        if arr[j][i] == '|':
            if flag == 0:
                flag = 1
        if arr[j][i] == '-' and flag == 1:
            flag = 0
            cnt += 1
    if flag:
        flag = 0
        cnt += 1
print(cnt)


