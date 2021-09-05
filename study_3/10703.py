# 1. 한 줄 이상의 공기 (.)
# 2. 유성은 X로 그 위에
# 3. 땅은 #로 그 아래
# 유성 모양을 리스트에 저장
# 가장 짧은 유성과 땅의 거리를 찾아서 그것만큼 모든 유성의 y값을 내려주면 된다.
import sys
sys.stdin = open('10703_input.txt')
R, S = map(int, input().split())
pic = [list(input()) for _ in range(R)]
star = [[] for _ in range(S)]
ground = [R] * S
for i in range(R):
    for j in range(S):
        if pic[i][j] == 'X':
            star[j].append(i)
            pic[i][j] = '.'
        elif pic[i][j] == '#':
            if ground[j] == R:
                ground[j] = i

d = R
for i in range(S):
    if star[i] and d > ground[i] - max(star[i]):
        d = ground[i] - max(star[i])
for i in range(S):
    for j in range(len(star[i])):
        pic[star[i][j]+d-1][i] = 'X'
for i in range(R):
    print(''.join(pic[i]))

