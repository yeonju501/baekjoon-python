# 세로 가로로 숫자 받음
# 상태 입력 받음 바깥 포문이 세로 안쪽 포문이 가로
# count x개수 없으면 +1 
height, width = map(int, input().split())
castle = []
for i in range(height):
    castle.append(input())
guardi = []
guardj = []
for i in range(len(castle)):
    for j in range(len(castle[i])):
        if castle[i][j] =='X':
            guardi.append(i)
            guardj.append(j)
print(castle)
print(guardi)
print(guardj)
# 만약에 i가 없으면 더해 0 j도 없으면 더해
guard = 0
for i in range(height):
    for j in range(width):
        if i not in guardi and j not in guardj:
            guard += 1
            guardi.append(i)
            guardj.append(j)
print(guard)







