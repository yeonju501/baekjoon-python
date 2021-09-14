
import sys
sys.stdin = open('1236_input.txt')

N, M = map(int, input().split())
# .은 빈칸 X는 경비원
arr = [list(input()) for _ in range(N)]
cnt = 0
cnt1 = 0
x = [0] * N
y = [0] * M
for i in range(M):
    flag = 0
    for j in range(N):
        if arr[j][i] == 'X':
            flag = 1
    if flag == 0:
        cnt += 1

for i in range(N):
    flag = 0
    for j in range(M):
        if arr[i][j] == 'X':
            flag = 1
    if flag == 0:
        cnt1 += 1
print(max(cnt, cnt1))









