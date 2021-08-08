# 이차원배열을 채워준다 0으로 그리고 1 2로 채우자
# 대각선 (1,1 2,2 3,3), (1,3 2,2, 3,1)
# 행방향 (1,1 1,2 1,3) (2,1 2,2 2,3) (3,1 3,2 3,3)
# 열방향 (1,1 2,1 3,1) (1,2 2,2 3,2) (1,3 2,3 3,3)
# 나오는 같은 숫자가 3번 나오면 이긴다 x나 y가
# 대각선은?
# 검사를 해야한다. 6번을 받아서 확인 나머지 세개를 입력 받아서 확인?

import sys
t = int(input())
one_x = []
one_y = []
two_x = []
two_y = []
for i in range(1, 10):
    x, y= map(int, input().split())
    if i % 2:
        one_x.append(x)
        one_y.append(y)
    else:
        two_x.append(x)
        two_y.append(y)

