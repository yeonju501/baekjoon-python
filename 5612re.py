# 3시간 2개의 차
# 1분간 입구를 통과한 차 2대 출구를 통과한 차 3대
# j분 지난 시점 터널 안에 있는 차량의 수 S의 최대값
# 차량의 수가 한 번이라도 작았다면 0 출력
n = int(input())
m = int(input())
max_p = m
for j in range(n):
    a, b = map(int,input().split())
    m = m + a - b
    if m < 0:
        max_p = 0
        break
    if max_p < m :
        max_p = m
print(max_p)        