# 0부터 9 순서 섞음.
import sys
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
score_a = 0
score_b = 0
draw = []
for i in range(10):
    if a[i] > b[i]:
        score_a += 3
        win = 'A'
    elif b[i] > a[i]:
        score_b += 3
        win = 'B'
    else:
        score_b += 1
        score_a += 1
print(score_a, score_b)
if score_a > score_b:
    print('A')
elif score_b > score_a:
    print('B')
else :
    if a == b:
        print('D')
    else:
        print(win)
