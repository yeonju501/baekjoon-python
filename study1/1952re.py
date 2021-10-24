M, N = map(int,input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = y = 0
mode = 0
snail = [[0]*N for i in range(M)]
snail[x][y] = 1
s = 1
cnt = 0
for i in range(2, N*M+1):
    x += dx[mode]
    y += dy[mode]
    snail[x][y] = i
    if i == N*M:
        break
    if 0 <= x + dx[mode] < M and 0 <= y + dy[mode] < N and not snail[x+dx[mode]][y+dy[mode]]:
        continue
    if mode != 3:
        cnt += 1
        mode += 1
    else:
        mode = 0
# for i in snail:
#     print(*i)
print(cnt)

# M 행
# N 열
if M == N or M < N:
    result = M*2-2
else: 
    result = N*2-1
print(result)
